from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..models.user import User
from ..database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def role_checker(required_role: str):
    def role_dependency(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
        if current_user.role.name != required_role:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Insufficient permissions")
        return current_user
    return role_dependency
