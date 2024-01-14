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
from .routes.ticket import router as ticket_router

from apscheduler.schedulers.background import BackgroundScheduler
from services.crud_product import check_and_notify_low_stock
from database import SessionLocal
from models.product import Product
from services.email_service import send_email
from models.user import User




def check_stock():
    db = SessionLocal()
    products = db.query(Product).all()
    for product in products:
        check_and_notify_low_stock(db, product.id)
    db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(check_stock, 'interval', hours=24)
scheduler.start()

def send_marketing_emails():
    db = SessionLocal()
    try:
        users = db.query(User).filter(User.is_subscribed == True).all()  # 假设有一个 is_subscribed 字段
        for user in users:
            send_email(
                subject="Check out our new products!",
                body="<strong>Exciting new products just for you.</strong>",
                to_email=user.email
            )
    finally:
        db.close()

scheduler = BackgroundScheduler()
scheduler.add_job(send_marketing_emails, 'cron', day_of_week='mon', hour=8)  # 每周一上午8点发送
scheduler.start()

app = FastAPI()

app.include_router(user_router)
app.include_router(role_router)
app.include_router(product_router)
app.include_router(order_router)
app.include_router(stripe_router)
app.include_router(alipay_router)
app.include_router(wechatpay_router)
app.include_router(crypto_router)
app.include_router(ticket_router, prefix="/api/v1", tags=["tickets"])

