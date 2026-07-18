from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.security.security import hash_password


def create_user(db: Session, user: UserCreate):

    # Check if email already exists
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        return None

    db_user = User(
        fullname=user.fullname,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

from app.security.security import verify_password
from app.security.jwt_handler import create_access_token


def authenticate_user(db: Session, email: str, password: str):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    return user


def login_user(db: Session, email: str, password: str):

    user = authenticate_user(db, email, password)

    if user is None:
        return None

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
