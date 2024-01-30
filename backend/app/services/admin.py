# crud/admin.py
from sqlalchemy.orm import Session
from ..models.admin import Admin, AdminRole

def create_admin(db: Session, admin_data: dict):
    db_admin = Admin(**admin_data)
    db.add(db_admin)
    db.commit()
    db.refresh(db_admin)
    return db_admin

def get_admin(db: Session, admin_id: int):
    return db.query(Admin).filter(Admin.id == admin_id).first()

def get_admins(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Admin).offset(skip).limit(limit).all()

def update_admin(db: Session, admin_id: int, admin_data: dict):
    db.query(Admin).filter(Admin.id == admin_id).update(admin_data)
    db.commit()
    return db.query(Admin).filter(Admin.id == admin_id).first()

def delete_admin(db: Session, admin_id: int):
    db_admin = db.query(Admin).filter(Admin.id == admin_id).first()
    db.delete(db_admin)
    db.commit()
    return db_admin

