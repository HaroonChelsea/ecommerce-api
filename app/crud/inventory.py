from sqlalchemy.orm import Session
from app.db.models import Inventory
from app.db.schemas import InventoryCreate
import datetime


def create_inventory(db: Session, item: InventoryCreate):
    new_inventory = Inventory(
        product_id=item.product_id,
        stock_level=item.stock_level,
        updated_at=datetime.datetime.utcnow(),
    )
    db.add(new_inventory)
    db.commit()
    db.refresh(new_inventory)
    return new_inventory


def get_inventory_status(db: Session):
    return db.query(Inventory).all()


def get_low_stock_alerts(db: Session, threshold: int):
    return db.query(Inventory).filter(Inventory.stock_level < threshold).all()


def update_inventory_stock(db: Session, inventory_id: int, stock_level: int):
    item = db.query(Inventory).filter(Inventory.id == inventory_id).first()
    if item:
        item.stock_level = stock_level
        item.updated_at = datetime.datetime.utcnow()
        db.commit()
        db.refresh(item)
    return item
