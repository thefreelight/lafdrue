from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.role import RoleCreate, Role
from ..services.crud_role import create_role
from ..database import SessionLocal

router = APIRouter()

@router.post("/roles/", response_model=Role)
def create_role_view(role: RoleCreate, db: Session = Depends(SessionLocal)):
    db_role = create_role(db=db, role=role)
    return db_role
