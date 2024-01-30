# routers/admin.py
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from ..services.admin import get_admin, get_admins, create_admin
from ..schemas.admin import AdminCreate, Admin
from ..dependencies.database import get_db
from ..dependencies.security import verify_password, create_access_token
from datetime import datetime, timedelta

from ..dependencies.config import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/admins/", response_model=list[Admin])
def read_admins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    admins = get_admins(db, skip=skip, limit=limit)
    return admins

@router.get("/admins/{admin_id}", response_model=Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.post("/admins/", response_model=Admin)
def create_new_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    return create_admin(db=db, admin=admin)




@router.delete("/admins/{admin_id}", response_model=bool)
def delete_admin(admin_id: int, db: Session = Depends(get_db)):
    if delete_admin(db, admin_id):
        return True
    else:
        raise HTTPException(status_code=404, detail="Admin not found")

@router.put("/admins/{admin_id}", response_model=Admin)
def update_admin(admin_id: int, admin: AdminCreate, db: Session = Depends(get_db)):
    updated_admin = update_admin(db, admin_id, admin)
    if updated_admin is not None:
        return updated_admin
    else:
        raise HTTPException(status_code=404, detail="Admin not found")


@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    admin = db.query(Admin).filter(Admin.username == form_data.username).first()
    if not admin or not verify_password(form_data.password, admin.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(
        data={"sub": admin.username}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}