# routes/alipay.py
from fastapi import APIRouter, HTTPException
# 引入支付宝SDK
# from alipay import AliPay

router = APIRouter()

@router.post("/pay/alipay")
def pay_with_alipay(order_id: str, total_amount: float):
    # 初始化支付宝客户端
    alipay_client = AliPay(...)
    # 生成支付请求
    query = alipay_client.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=total_amount,
        subject="Order Payment",
        return_url="http://example.com/payments/alipay/return",
        notify_url="http://example.com/payments/alipay/notify"
    )
    # 返回支付链接
    pay_url = "https://openapi.alipaydev.com/gateway.do?" + query
    return {"pay_url": pay_url}
