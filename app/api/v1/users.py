from fastapi import APIRouter, Depends

from app.models.user import User
from app.security.auth import get_current_user

router = APIRouter(
    prefix="/api/v1/users",
    tags=["Users"],
)


@router.get("/me")
def get_me(
    current_user: User = Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "fullname": current_user.fullname,
        "email": current_user.email,
    }
