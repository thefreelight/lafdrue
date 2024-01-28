# main.py
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.database import engine, Base
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .routes import product
from .routes import category
from .routes import order
from .routes import payment_methods
from .routes import payment

app = FastAPI()


# 在启动应用前创建数据库表
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)




# 在这里定义异常处理器
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    print(f"OMG! The client sent invalid data!: {exc}")
    return JSONResponse(
        status_code=422,
        content={"detail": exc.errors()},
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

app.include_router(product.router, prefix="/api/v1", tags=["products"])
app.include_router(category.router, prefix="/api/v1", tags=["categories"])
app.include_router(order.router, prefix="/api/v1", tags=["orders"])
app.include_router(payment_methods.router, prefix="/api/v1", tags=["payment-methods"])
app.include_router(payment.router, prefix="/api/v1", tags=["payments"])

