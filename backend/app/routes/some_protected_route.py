from fastapi import APIRouter, Depends
from ..dependencies.role_checker import role_checker
from ..models.user import User

router = APIRouter()

@router.get("/protected-route/")
async def protected_route(current_user: User = Depends(role_checker("admin"))):
    return {"message": "只有管理员可以访问这个路由"}
