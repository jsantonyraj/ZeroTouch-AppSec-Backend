from sqlalchemy import Column, Integer, String

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100))
    email = Column(String(100), unique=True, index=True)
    password = Column(String(255))
