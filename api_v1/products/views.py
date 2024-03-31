from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper
from . import crud
from .schemas import Product, ProductCreate, ProductUpdate
from .dependencies import get_product_by_id

router = APIRouter()


@router.get("/", response_model=list[Product])
async def get_products(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.get_products(session=session)


@router.post("/", response_model=Product)
async def create_product(
        product_in: ProductCreate,
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.create_product(session=session, product_in=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product_by_id(
        product: Product = Depends(get_product_by_id)
):
    return product


@router.put("/{product_id}/}", response_model=Product)
async def update_product(
        product_update: ProductUpdate,
        product: Product = Depends(get_product_by_id),
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    return await crud.update_product(session=session, product=product, product_update=product_update)
