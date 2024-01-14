from sqlalchemy.orm import Session
from ..models.role import Role
from ..schemas.role import RoleCreate

def create_role(db: Session, role: RoleCreate):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role

# 添加更多操作，如获取角色、更新角色等
