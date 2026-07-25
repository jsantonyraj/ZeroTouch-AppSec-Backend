from sqlalchemy.orm import Session

from app.models.organization import Organization
from app.schemas.organization import OrganizationCreate


def create_organization(
    db: Session,
    organization: OrganizationCreate,
    created_by: str,
):

    existing = (
        db.query(Organization)
        .filter(Organization.name == organization.name)
        .first()
    )

    if existing:
        return None

    org = Organization(
        name=organization.name,
        description=organization.description,
        website=organization.website,
        created_by=created_by,
    )

    db.add(org)
    db.commit()
    db.refresh(org)

    return org


def get_all_organizations(db: Session):
    return db.query(Organization).all()
