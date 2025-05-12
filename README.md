# 🛍️ E-commerce Admin API

FastAPI-powered backend for admin dashboards that manage product sales, inventory, and revenue tracking.

---

## 🚀 Features Implemented

### 📊 Sales Status

- `POST /sales` – Record a sale
- `GET /sales` – Retrieve filtered sales
  - Filters: `start_date`, `end_date`, `product_id`, `category`
- `GET /revenue` – Aggregate revenue by `daily`, `weekly`, `monthly`, or `yearly`

### 📦 Inventory Management

- `POST /inventory` – Add inventory for product
- `GET /inventory` – View inventory levels
- `GET /inventory/low-stock` – Get products below stock threshold
- `PATCH /inventory/{inventory_id}` – Update stock level

### 🛒 Product Management

- `POST /products` – Create new product

---

## 🧪 Demo Data

Load demo data with:

```bash
PYTHONPATH=. python scripts/load_demo_data.py
```

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
$ git clone <repo_url>
$ cd ecommerce-api

# Create virtual environment
$ pyenv virtualenv 3.11.9 ecommerce-api
$ pyenv activate ecommerce-api

# Install dependencies
$ pip install -r requirements.txt

# Start server
$ uvicorn app.main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI

---

## 🧱 Tech Stack

- Python 3.11 + FastAPI
- SQLAlchemy ORM + MySQL
- Pydantic (v2 compliant)
- Uvicorn ASGI server

---

## 📁 Project Structure

```
app/
  ├── api/           # Routes
  ├── crud/          # Business logic
  ├── db/            # Models, schemas, sessions
  ├── core/          # Settings loader
scripts/              # Demo data loader
```
