from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class Organization(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(150), nullable=False, unique=True)

    description = Column(String(500))

    website = Column(String(200))

    created_by = Column(String(150))

    # Relationship with Project
    projects = relationship(
        "Project",
        back_populates="organization",
        cascade="all, delete-orphan",
    )
