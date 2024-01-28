from fastapi import APIRouter, Depends, HTTPException,Request
from sqlalchemy.orm import Session
from ..schemas.order import OrderSchema
from ..services.order import create_order
from ..dependencies.database import get_db
from pydantic import ValidationError


router = APIRouter()

@router.post("/creat_order/", response_model=OrderSchema)
async def create_order_endpoint(order_create: OrderSchema, db: Session = Depends(get_db)):
    try:
        created_order = create_order(db=db, order_create=order_create)
        db.commit()
        return created_order
    except Exception as e:
        print(e)
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    except ValidationError as e:
        # 这里捕获Pydantic的验证错误，并返回具体的错误信息
        raise HTTPException(status_code=422, detail=e.errors())

