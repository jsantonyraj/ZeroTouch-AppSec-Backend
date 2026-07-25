from pydantic import BaseModel


class OrganizationCreate(BaseModel):
    name: str
    description: str | None = None
    website: str | None = None


class OrganizationResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    website: str | None = None
    created_by: str | None = None

    class Config:
        from_attributes = True
