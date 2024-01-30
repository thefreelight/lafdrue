from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from ..dependencies.database import get_db
from ..models.order import Order,PaymentStatus,ShippingStatus
from ..services.payments.yipay_processor import YiPayProcessor

router = APIRouter()

async def handle_yipay_notification(data: dict, db: AsyncSession):
    # 验证签名的逻辑
    params = {k: v for k, v in data.items() if v is not None}
    sign = params.pop('sign', None)
    local_sign = YiPayProcessor.generate_md5_sign(params)

    if local_sign != sign:
        raise ValueError("Invalid signature")

    # 验证交易状态
    if params.get("trade_status") == "TRADE_SUCCESS":
        # 交易成功，更新订单状态
        out_trade_no = params.get("out_trade_no")
        order = await db.query(Order).filter_by(order_number=out_trade_no).first()
        if order:
            order.payment_status = PaymentStatus.PAID.value
            order.shipping_status = ShippingStatus.SENT.value
            await db.commit()
        else:
            raise ValueError("Order not found")
        return "success"
    else:
        return "fail"

@router.post("/payment-notification/")
async def payment_notification(request: Request, db: AsyncSession = Depends(get_db)):
    notification_data = await request.json()
    payment_method = notification_data.get('type')

    if payment_method == 'yipay':
        response = await handle_yipay_notification(notification_data, db)
        return {"status": response}
    else:
        raise HTTPException(status_code=400, detail="Unsupported payment method")
