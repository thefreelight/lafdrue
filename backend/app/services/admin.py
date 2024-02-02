from sqlalchemy.orm import Session
from ..models.admin import Admin,AdminRole
from passlib.context import CryptContext
from ..schemas.admin import AdminCreate
from ..schemas.admin import AdminRoleCreate, AdminRoleUpdate
from typing import Optional


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 创建新角色
def create_admin_role(db: Session, admin_role: AdminRoleCreate):
    new_role = AdminRole(name=admin_role.name, permissions=admin_role.permissions)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

# 获取角色列表
def get_admin_roles(db: Session, skip: int = 0, limit: int = 100) -> list[AdminRole]:
    return db.query(AdminRole).offset(skip).limit(limit).all()

# 获取单个角色
def get_admin_role(db: Session, role_id: int) -> Optional[AdminRole]:
    return db.query(AdminRole).filter(AdminRole.id == role_id).first()

# 更新角色
def update_admin_role(db: Session, role_id: int, role: AdminRoleUpdate) -> AdminRole:
    db_role = db.query(AdminRole).filter(AdminRole.id == role_id).first()
    if not db_role:
        return None
    update_data = role.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_role, key, value)
    db.commit()
    db.refresh(db_role)
    return db_role

# 删除角色
def delete_admin_role(db: Session, role_id: int) -> bool:
    db_role = db.query(AdminRole).filter(AdminRole.id == role_id).first()
    if not db_role:
        return False
    db.delete(db_role)
    db.commit()
    return True

def get_admin(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.id == admin_id).first()

def get_admin_by_email(db: Session, email: str):
    return db.query(Admin).filter(Admin.email == email).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Admin).offset(skip).limit(limit).all()

def create_admin(db: Session, admin: AdminCreate):
    hashed_password = pwd_context.hash(admin.password)
    db_admin = Admin(email=admin.email, hashed_password=hashed_password, username=admin.username, role_id=admin.role_id)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def delete_admin(db: Session, admin_id: int):
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin:
        db.delete(db_admin)
        db.commit()
        return True
    return False

def update_admin(db: Session, admin_id: int, admin: AdminCreate):
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    if db_admin:
        db_admin.email = admin.email
        db_admin.username = admin.username
        db_admin.role_id = admin.role_id
        db_admin.hashed_password = pwd_context.hash(admin.password) if admin.password else db_admin.hashed_password
        db.commit()
        db.refresh(db_admin)
        return db_admin
    return None


