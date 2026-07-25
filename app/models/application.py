import uuid

from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)

    uuid = Column(
        String(36),
        unique=True,
        nullable=False,
        default=lambda: str(uuid.uuid4())
    )

    application_name = Column(String(255), nullable=False)
    application_code = Column(String(100), unique=True, nullable=False)

    description = Column(Text)

    application_type = Column(String(100), nullable=False)

    environment = Column(String(50), nullable=False)

    criticality = Column(String(50), nullable=False)

    business_owner = Column(String(255))

    technical_owner = Column(String(255))

    technology_stack = Column(String(255))

    internet_facing = Column(Boolean, default=False)

    authentication_type = Column(String(100))

    compliance_tags = Column(String(255))

    lifecycle = Column(String(100), default="Development")

    status = Column(String(50), default="Active")

    project_id = Column(
        Integer,
        ForeignKey("projects.id"),
        nullable=False
    )

    created_by = Column(String(255))

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    project = relationship(
        "Project",
        back_populates="applications"
    )
