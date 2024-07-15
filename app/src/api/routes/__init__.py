from fastapi import APIRouter, Depends
from . import category, supplier, product, auth
from app.src.api.routes.validated_token import token_required

# dependencies=[Depends(token_required)]

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["auth"])
# router.include_router(category.router, prefix="/categories", tags=["categories"])
# router.include_router(supplier.router, prefix="/suppliers", tags=["suppliers"])
# router.include_router(product.router, prefix="/products", tags=["products"])