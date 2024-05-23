from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..dependencies.config import ACCESS_TOKEN_EXPIRE_MINUTES
from ..models.admin import Admin
from ..models.user import User
from ..services.auth_service import verify_password, create_access_token
from datetime import timedelta


router = APIRouter()


@router.post("/token/")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 尝试查询管理员
    admin = db.query(Admin).filter(Admin.email == form_data.username).first()
    if admin and verify_password(form_data.password, admin.hashed_password):
        user_info = admin
    else:
        # 若未找到管理员，尝试查询普通用户
        user = db.query(User).filter(User.email == form_data.username).first()
        if user and verify_password(form_data.password, user.hashed_password):
            user_info = user
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="用户名或者密码错误",
                headers={"WWW-Authenticate": "Bearer"},
            )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user_info.email}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}