from fastapi import APIRouter, Depends, status, HTTPException

from model.exchange_rate import ExchangeRate
from schema.exchange_rate import ExchangeRateFullSchema, ExchangeRateParamsSchema, ExchangeRateSmallSchema
from schema.pagination import PaginationResponseSchema
from repository.exchange_rate import ExchangeRateData
from settings.database import get_session


router = APIRouter(prefix='/exchange_rate', tags=['ExchangeRate'])


@router.get('/', response_model=PaginationResponseSchema[ExchangeRateFullSchema])
async def exchange_rate_list(
                                pagination = Depends(ExchangeRateParamsSchema),
                                session = Depends(get_session),
                            ):
    """Получить список обмена валют с пагинацией и сортировкой

    параметры пагинации:
    - Страница: ?page=0
    - Количество записей на странице: ?page_size=20

    Параметры сортировки:
    - Сортировка по ID: ?sort_field=поле сортировки
      Пример сортировки по id: ?sort_field=id
    - Порядок сортировка: ?sort_order=asc (увеличение) или desc (уменьшение)

    Параметры фильтров:
    - Фильтр по id: ?id=1
    - Фильтр по точной дате: ?date=
    - Фильтр для даты больше: date_gte=
    - Фильтр для даты меньше: date_lte=
    - Фильтр для id валюты: currency_id=2
    - Фильтр для id валюты к которой обмениваем: base_currency_id=3
    """
    try:
        exchage_rate_model = ExchangeRateData(ExchangeRate, session)
        exchage_rate_list, total = await exchage_rate_model.get_multi(
            skip=pagination.offset,
            limit=pagination.limit,
            sort_field=pagination.sort_field,
            sort_order=pagination.sort_order,
            filters=pagination.filters,
        )
        exchange_rate_schemes = [ExchangeRateFullSchema.model_validate(item) for item in exchage_rate_list]
        pages = pagination.get_count_pages(total)
        return PaginationResponseSchema[ExchangeRateFullSchema](
            items=exchange_rate_schemes,
            total=total,
            page=pagination.page,
            size=pagination.page_size,
            pages=pages
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
