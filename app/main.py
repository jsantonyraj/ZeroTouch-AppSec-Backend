from fastapi import FastAPI

from app.database.database import engine
from app.models.user import User

from app.api.v1.auth import router as auth_router

User.metadata.create_all(bind=engine)

app = FastAPI(
    title="ZeroTouch AppSec Cloud",
    description="Enterprise Application Security Platform",
    version="1.0.0"
)

app.include_router(auth_router)

@app.get("/")
def root():
    return {
        "product": "ZeroTouch AppSec Cloud",
        "version": "1.0.0",
        "status": "Running"
    }

@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }
