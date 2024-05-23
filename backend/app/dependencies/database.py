# backend/app/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:123456@db:3306/lafdrue"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_payment_service():
    # 在函数内部进行导入以避免循环引用
    from ..services.payment_methods import PaymentService
    # 接下来创建和返回 PaymentService 实例
    payment_service = PaymentService()
    return payment_service