from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from ..schemas.order import OrderCreateSchema
from ..services.order import create_order
from ..dependencies.database import get_db

router = APIRouter()

@router.post("/orders/", response_model=OrderCreateSchema)
async def create_order_endpoint(request: Request, db: Session = Depends(get_db)):
    print(f"Request headers: {request.headers}")
    print(f"Request body: {await request.json()}")

    try:
        order_create = await request.json()
        return create_order(db=db, order_create=order_create)
    except Exception as e:
        db.rollback()  # 发生异常时回滚数据库事务
        print(f"Error creating order: {e}")  # 打印错误信息
        raise HTTPException(status_code=400, detail=str(e))
