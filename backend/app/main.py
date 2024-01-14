# main.py
from fastapi import FastAPI
from .routes.user import router as user_router
from .routes.role import router as role_router
from .routes.product import router as product_router
from .routes.order import router as order_router
from .routes.pay.stripe import router as stripe_router
from .routes.pay.alipay import router as alipay_router
from .routes.pay.wechatpay import router as wechatpay_router
from .routes.pay.crypto import router as crypto_router

app = FastAPI()

app.include_router(user_router)
app.include_router(role_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(stripe_router)
app.include_router(alipay_router)
app.include_router(wechatpay_router)
app.include_router(crypto_router)
