from sqlalchemy.orm import Session
from app.db.models import Sale, Product
from app.db.schemas import SaleCreate
from sqlalchemy import func, text
import datetime


def create_sale(db: Session, item: SaleCreate):
    new_sale = Sale(
        product_id=item.product_id,
        quantity=item.quantity,
        total_amount=item.total_amount,
        sold_at=datetime.datetime.utcnow(),
    )
    db.add(new_sale)
    db.commit()
    db.refresh(new_sale)
    return new_sale


def get_filtered_sales(
    db: Session, start_date=None, end_date=None, category=None, product_id=None
):
    query = db.query(Sale).join(Product)

    if start_date:
        query = query.filter(Sale.sold_at >= start_date)
    if end_date:
        query = query.filter(Sale.sold_at <= end_date)
    if category:
        query = query.filter(Product.category == category)
    if product_id:
        query = query.filter(Sale.product_id == product_id)

    return query.all()


def get_revenue_by_period(db: Session, period: str):
    date_formats = {
        "daily": "%Y-%m-%d",
        "weekly": "%Y-%u",
        "monthly": "%Y-%m",
        "yearly": "%Y",
    }

    fmt = date_formats.get(period, "%Y-%m-%d")

    results = (
        db.query(
            func.sum(Sale.total_amount).label("total_revenue"),
            func.date_format(Sale.sold_at, fmt).label("period"),
        )
        .group_by("period")
        .order_by("period")
        .all()
    )

    return [
        {"period": row.period, "total_revenue": float(row.total_revenue)}
        for row in results
    ]
