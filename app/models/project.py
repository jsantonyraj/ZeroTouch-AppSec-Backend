from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    project_name = Column(String(150), nullable=False)
    project_code = Column(String(50), unique=True, nullable=False)
    description = Column(String(500))
    environment = Column(String(50), default="DEV")
    status = Column(String(30), default="Active")

    organization_id = Column(
        Integer,
        ForeignKey("organizations.id"),
        nullable=False,
    )

    created_by = Column(String(150))

    organization = relationship(
        "Organization",
        back_populates="projects",
    )

    applications = relationship(
        "Application",
        back_populates="project",
        cascade="all, delete-orphan",
    )
