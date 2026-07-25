from fastapi import FastAPI
from app.api.v1.users import router as users_router
from app.database.database import engine
from app.models.user import User
from app.models.organization import Organization
from app.api.v1.auth import router as auth_router
from app.api.v1.project import router as project_router
from app.api.v1.organizations import router as organization_router
from app.database.database import Base

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ZeroTouch AppSec Cloud",
    description="Enterprise Application Security Platform",
    version="1.0.0"
)

app.include_router(auth_router)
app.include_router(users_router)
app.include_router(organization_router)
app.include_router(project_router)
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
