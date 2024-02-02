from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services import admin as admin_services
from ..schemas.admin import AdminCreate, Admin,AdminRole,AdminRoleUpdate,AdminRoleCreate
from ..services.admin import create_admin_role, get_admin_role, get_admin_roles, update_admin_role, delete_admin_role
from ..dependencies.database import get_db
from typing import List

router = APIRouter()

@router.post("/admin/roles/", response_model=AdminRole)
def create_role(admin_role: AdminRoleCreate, db: Session = Depends(get_db)):
    return create_admin_role(db=db, admin_role=admin_role)

@router.get("/admin/roles/", response_model=List[AdminRole])
def read_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    roles = get_admin_roles(db, skip=skip, limit=limit)
    return roles

@router.get("/admin/roles/{role_id}", response_model=AdminRole)
def read_role(role_id: int, db: Session = Depends(get_db)):
    db_role = get_admin_role(db, role_id=role_id)
    if db_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return db_role

@router.put("/admin/roles/{role_id}", response_model=AdminRole)
def update_role(role_id: int, admin_role: AdminRoleUpdate, db: Session = Depends(get_db)):
    updated_role = update_admin_role(db, role_id=role_id, admin_role=admin_role)
    if updated_role is None:
        raise HTTPException(status_code=404, detail="Role not found")
    return updated_role

@router.delete("/admin/roles/{role_id}", response_model=bool)
def delete_role(role_id: int, db: Session = Depends(get_db)):
    if not delete_admin_role(db, role_id):
        raise HTTPException(status_code=404, detail="Role not found")
    return True

@router.get("/admins/", response_model=List[Admin])
def read_admins(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    admins = admin_services.get_admins(db, skip=skip, limit=limit)
    return admins

@router.get("/admins/{admin_id}", response_model=Admin)
def read_admin(admin_id: int, db: Session = Depends(get_db)):
    db_admin = admin_services.get_admin(db, admin_id=admin_id)
    if db_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return db_admin

@router.post("/admins/", response_model=Admin)
def create_admin(admin: AdminCreate, db: Session = Depends(get_db)):
    db_admin = admin_services.get_admin_by_email(db, email=admin.email)
    if db_admin:
        raise HTTPException(status_code=400, detail="Email already registered")
    return admin_services.create_admin(db=db, admin=admin)

@router.delete("/admins/{admin_id}", response_model=bool)
def delete_admin_route(admin_id: int, db: Session = Depends(get_db)):
    if not admin_services.delete_admin(db, admin_id):
        raise HTTPException(status_code=404, detail="Admin not found")
    return True

@router.put("/admins/{admin_id}", response_model=Admin)
def update_admin_route(admin_id: int, admin: AdminCreate, db: Session = Depends(get_db)):
    updated_admin = admin_services.update_admin(db, admin_id, admin)
    if updated_admin is None:
        raise HTTPException(status_code=404, detail="Admin not found")
    return updated_admin
