from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.dependencies import get_db
from app.models.user import User
from app.schemas.organization import (
    OrganizationCreate,
    OrganizationResponse,
)
from app.security.auth import get_current_user
from app.services.organization_service import (
    create_organization,
    get_all_organizations,
)

router = APIRouter(
    prefix="/api/v1/organizations",
    tags=["Organizations"],
)


@router.post(
    "",
    response_model=OrganizationResponse,
)
def create(
    organization: OrganizationCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    org = create_organization(
        db=db,
        organization=organization,
        created_by=current_user.email,
    )

    if org is None:
        raise HTTPException(
            status_code=400,
            detail="Organization already exists",
        )

    return org


@router.get(
    "",
    response_model=list[OrganizationResponse],
)
def get_all(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_all_organizations(db)
