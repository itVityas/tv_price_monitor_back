from fastapi import APIRouter, Depends, status, HTTPException

from settings.database import get_session
from model.shop_link import ShopLink
from repository.shop_link import ShopLinkData
from schema.pagination import PaginationResponseSchema
from schema.shop_link import (
    ShopLinkFilterSchema,
    ShopLinkPostSchema,
    ShopLinkResponceFullSchema,
    ShopLinkUpdateSchema,
    ShopLinkResponceSmallSchema,
)


router = APIRouter(prefix='/shop_link', tags=['ShopLink'])


@router.get('/', response_model=PaginationResponseSchema[ShopLinkResponceFullSchema])
async def shop_link_list(pagination: ShopLinkFilterSchema = Depends(), session=Depends(get_session)):
    try:
        shop_link_data = ShopLinkData(ShopLink, session)
        shop_link_list, total = await shop_link_data.get_multi(
            skip=pagination.offset,
            limit=pagination.limit,
            sort_field=pagination.sort_field,
            sort_order=pagination.sort_order,
            filters=pagination.filters,
            eager_loads=[
                'shop',
                'tv',
            ]
        )
        shop_link_schemes = [ShopLinkResponceFullSchema.model_validate(item) for item in shop_link_list]
        pages = pagination.get_count_pages(total)
        return PaginationResponseSchema[ShopLinkResponceFullSchema](
            items=shop_link_schemes,
            total=total,
            page=pagination.page,
            size=pagination.page_size,
            pages=pages
        )
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post('/', response_model=ShopLinkResponceSmallSchema)
async def shop_link_create(shop_link: ShopLinkPostSchema, session=Depends(get_session)):
    try:
        shop_link_data = ShopLinkData(ShopLink, session)
        new_shop_link = await shop_link_data.create(shop_link)
        return ShopLinkResponceSmallSchema.model_validate(new_shop_link)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.patch('/patch/{id}/', response_model=ShopLinkResponceSmallSchema)
async def shop_link_update(id: int, shop_link: ShopLinkUpdateSchema, session=Depends(get_session)):
    try:
        shop_link_data = ShopLinkData(ShopLink, session)
        model = await shop_link_data.update(id, shop_link)
        return ShopLinkResponceSmallSchema.model_validate(model)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.delete('/delete/{id}/', status_code=status.HTTP_204_NO_CONTENT)
async def shop_link_delete(id: int, session=Depends(get_session)):
    try:
        shop_link_data = ShopLinkData(ShopLink, session)
        await shop_link_data.delete(id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
