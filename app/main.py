from fastapi import FastAPI
from app.api.routes import router
from app.db.session import engine, Base

app = FastAPI(title="E-commerce Admin API")

# Create tables on startup (Dev only)
Base.metadata.create_all(bind=engine)

app.include_router(router)


@app.get("/")
def root():
    return {"message": "E-commerce API is running!"}
