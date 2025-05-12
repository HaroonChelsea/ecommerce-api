from app.db.session import SessionLocal
from app.db.models import Product, Inventory, Sale
import datetime


def load_data():
    db = SessionLocal()
    try:
        # Create products
        p1 = Product(name="Amazon Echo", category="Electronics", price=120.0)
        p2 = Product(name="Walmart Blender", category="Appliances", price=45.5)

        db.add_all([p1, p2])
        db.commit()
        db.refresh(p1)
        db.refresh(p2)

        # Add inventory
        i1 = Inventory(product_id=p1.id, stock_level=50)
        i2 = Inventory(product_id=p2.id, stock_level=30)

        db.add_all([i1, i2])
        db.commit()

        # Add sales
        s1 = Sale(product_id=p1.id, quantity=3, total_amount=360.0)
        s2 = Sale(product_id=p2.id, quantity=2, total_amount=91.0)

        db.add_all([s1, s2])
        db.commit()

        print("✅ Demo data loaded successfully.")
    finally:
        db.close()


if __name__ == "__main__":
    load_data()
