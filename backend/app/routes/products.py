from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, selectinload

from ..database import get_db
from ..models import Product
from ..schemas import ProductResponse
from ..review_data import get_amazon_review_analysis


router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.get("", response_model=list[ProductResponse])
@router.get("/", response_model=list[ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):
    products = db.query(Product).options(selectinload(Product.reviews)).all()
    results = []
    for p in products:
        results.append({
            "id": p.id,
            "merchant_id": p.merchant_id,
            "title": p.title,
            "price": p.price,
            "stock": p.stock,
            "attributes": p.attributes,
            "delivery_eta": p.delivery_eta,
            "image_url": p.image_url,
            "reviews": p.reviews,
            "review_analysis": get_amazon_review_analysis(p.title, p.reviews, p.attributes),
        })
    return results


@router.get("/{product_id}", response_model=ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .options(selectinload(Product.reviews))
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    return {
        "id": product.id,
        "merchant_id": product.merchant_id,
        "title": product.title,
        "price": product.price,
        "stock": product.stock,
        "attributes": product.attributes,
        "delivery_eta": product.delivery_eta,
        "image_url": product.image_url,
        "reviews": product.reviews,
        "review_analysis": get_amazon_review_analysis(product.title, product.reviews, product.attributes),
    }



@router.patch("/{product_id}/stock", response_model=ProductResponse)
def update_product_stock(
    product_id: int,
    stock: int,
    db: Session = Depends(get_db)
):
    """
    Update live inventory for a product.
    Allows judges and testers to trigger out-of-stock failure directly in DB.
    """
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.stock = max(0, stock)
    db.commit()
    db.refresh(product)

    return product