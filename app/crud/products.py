from sqlalchemy.orm import Session
from app.db.models import Product
from app.db.schemas import ProductCreate
import datetime


def create_product(db: Session, product: ProductCreate):
    new_product = Product(
        name=product.name,
        category=product.category,
        price=product.price,
        created_at=datetime.datetime.utcnow(),
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
