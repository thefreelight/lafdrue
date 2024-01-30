from fastapi import APIRouter, Request, HTTPException, Depends
from sqlalchemy.orm import Session
from ..dependencies.database import get_db
from ..models.order import Order
from ..services.payments.yipay_processor import YiPayProcessor

router = APIRouter()

def handle_yipay_callback(data: dict, db: Session):
    # 验证签名的逻辑
    params = {k: v for k, v in data.items() if v is not None}
    sign = params.pop('sign', None)
    local_sign = YiPayProcessor.generate_md5_sign(params)

    if local_sign != sign:
        raise ValueError("Invalid signature")

    # 验证交易状态
    if params.get("trade_status") == "TRADE_SUCCESS":
        # 交易成功，检索订单
        out_trade_no = params.get("out_trade_no")
        order = db.query(Order).filter_by(order_number=out_trade_no).first()
        if order:
            # 在这里可以更新订单的某些状态，但通常这在通知接口中已经完成
            return {"status": "success", "message": "Payment successful", "order": order}
        else:
            return {"status": "fail", "message": "Order not found"}
    else:
        return {"status": "fail", "message": "Payment failed"}


@router.get("/payment-callback/")
async def payment_callback(request: Request, db: Session = Depends(get_db)):
    callback_data = request.query_params
    payment_method = callback_data.get('type')

    if payment_method == 'yipay':
        return handle_yipay_callback(callback_data, db)
    elif payment_method == 'alipay':
        pass  # 处理支付宝回调的逻辑...
    else:
        raise HTTPException(status_code=400, detail="Unsupported payment method")

    return {"status": "success", "message": "Callback processed"}
