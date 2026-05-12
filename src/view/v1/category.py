from fastapi import APIRouter, Depends, status, HTTPException

from settings.database import get_session
from model.category import Category
from repository.category import CategoryData
from schema.pagination import PaginationResponseSchema
from schema.category import (
    CategoryFullSchema,
    CategorySmallSchema,
    CategoryUpdateSchema,
    CategoryParamsSchema
)

router = APIRouter(prefix='/category', tags=['Category'])


@router.get('/', response_model=PaginationResponseSchema[CategoryFullSchema])
async def category_list(pagination: CategoryParamsSchema = Depends(), session=Depends(get_session)):
    """Получить список категорий с пагинацией, сортировкой и фильтрацией

    параметры пагинации:
    - Страница: ?page=0
    - Количество записей на странице: ?page_size=20

    Параметры сортировки:
    - Сортировка по ID: ?sort_field=поле сортировки
      Пример сортировки по id: ?sort_field=id
    - Порядок сортировка: ?sort_order=asc (увеличение) или desc (уменьшение)

    Параметры фильтров:
    - Фильтр по id: ?id=1
    - Фильтр по названию: ?name=смарт
    - Точное совпадение названия: ?name=смарт
    - Название не равно: ?name_ne=смарт
    - Название содержит подстроку: ?name_icontains=смарт
    - Название начинается с: ?name_istartswith=смарт
    - Название заканчивается на: ?name_iendswith=смарт
    """
    try:
        category_data = CategoryData(Category, session)
        category_list, total = await category_data.get_multi(
            skip=pagination.offset,
            limit=pagination.limit,
            sort_field=pagination.sort_field,
            sort_order=pagination.sort_order,
            filters=pagination.filters,)
        category_schemes = [CategoryFullSchema.model_validate(item) for item in category_list]
        pages = pagination.get_count_pages(total)
        return PaginationResponseSchema[CategoryFullSchema](
            items=category_schemes,
            total=total,
            page=pagination.page,
            size=pagination.page_size,
            pages=pages
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post('/', response_model=CategoryFullSchema)
async def category_create(category: CategorySmallSchema, session=Depends(get_session)):
    try:
        category_data = CategoryData(Category, session)
        new_category = await category_data.create(category)
        return CategoryFullSchema.model_validate(new_category)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch('/patch/{id}/', response_model=CategoryFullSchema)
async def category_update(id: int, category: CategoryUpdateSchema, session=Depends(get_session)):
    try:
        category_data = CategoryData(Category, session)
        model = await category_data.update(id, category)
        return CategoryFullSchema.model_validate(model)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete('/delete/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def category_delete(id: int, session=Depends(get_session)):
    try:
        category_data = CategoryData(Category, session)
        await category_data.delete(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
