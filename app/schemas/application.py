from typing import Optional

from pydantic import BaseModel, ConfigDict


class ApplicationBase(BaseModel):
    application_name: str
    application_code: str
    description: Optional[str] = None

    application_type: str
    environment: str
    criticality: str

    business_owner: Optional[str] = None
    technical_owner: Optional[str] = None

    technology_stack: Optional[str] = None

    internet_facing: bool = False

    authentication_type: Optional[str] = None

    compliance_tags: Optional[str] = None

    lifecycle: Optional[str] = "Development"

    status: Optional[str] = "Active"

    project_id: int

    created_by: Optional[str] = None


class ApplicationCreate(ApplicationBase):
    pass


class ApplicationUpdate(BaseModel):
    application_name: Optional[str] = None
    description: Optional[str] = None
    application_type: Optional[str] = None
    environment: Optional[str] = None
    criticality: Optional[str] = None
    business_owner: Optional[str] = None
    technical_owner: Optional[str] = None
    technology_stack: Optional[str] = None
    internet_facing: Optional[bool] = None
    authentication_type: Optional[str] = None
    compliance_tags: Optional[str] = None
    lifecycle: Optional[str] = None
    status: Optional[str] = None


class ApplicationResponse(ApplicationBase):
    id: int
    uuid: str

    model_config = ConfigDict(from_attributes=True)
