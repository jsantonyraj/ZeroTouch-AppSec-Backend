from pydantic import BaseModel, Field
from typing import Optional


class ProjectCreate(BaseModel):
    project_name: str = Field(..., min_length=3, max_length=150)
    project_code: str = Field(..., min_length=2, max_length=50)
    description: Optional[str] = None
    environment: Optional[str] = "DEV"
    status: Optional[str] = "Active"
    organization_id: int


class ProjectUpdate(BaseModel):
    project_name: Optional[str] = None
    description: Optional[str] = None
    environment: Optional[str] = None
    status: Optional[str] = None


class ProjectResponse(BaseModel):
    id: int
    project_name: str
    project_code: str
    description: Optional[str]
    environment: Optional[str]
    status: Optional[str]
    organization_id: int
    created_by: Optional[str]

    class Config:
        from_attributes = True
