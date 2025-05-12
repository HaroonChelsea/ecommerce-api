from fastapi import APIRouter, Depends, Query, Path
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from app.db.session import SessionLocal
from app.db.schemas import ProductCreate, InventoryCreate, SaleCreate
from app.crud import products, inventory, sales

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/ping")
def ping():
    return {"message": "pong"}


@router.post("/products")
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    return products.create_product(db, product)


@router.post("/inventory")
def create_inventory(item: InventoryCreate, db: Session = Depends(get_db)):
    return inventory.create_inventory(db, item)


@router.post("/sales")
def create_sale(item: SaleCreate, db: Session = Depends(get_db)):
    return sales.create_sale(db, item)


@router.get("/sales")
def get_sales(
    db: Session = Depends(get_db),
    start_date: datetime = Query(None),
    end_date: datetime = Query(None),
    category: str = Query(None),
    product_id: int = Query(None),
):
    return sales.get_filtered_sales(db, start_date, end_date, category, product_id)


@router.get("/revenue")
def get_revenue(
    db: Session = Depends(get_db),
    period: str = Query("daily", enum=["daily", "weekly", "monthly", "yearly"]),
):
    return sales.get_revenue_by_period(db, period)


@router.get("/inventory")
def get_inventory(db: Session = Depends(get_db)):
    return inventory.get_inventory_status(db)


@router.get("/inventory/low-stock")
def get_low_stock(db: Session = Depends(get_db), threshold: int = Query(10)):
    return inventory.get_low_stock_alerts(db, threshold)


@router.patch("/inventory/{inventory_id}")
def update_inventory(
    inventory_id: int = Path(...),
    stock_level: int = Query(...),
    db: Session = Depends(get_db),
):
    return inventory.update_inventory_stock(db, inventory_id, stock_level)
