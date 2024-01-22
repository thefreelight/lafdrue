# main.py
from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.database import engine, Base
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from .routes import product
from .routes import category
from .routes import order

Base.metadata.create_all(bind=engine)  #创建数据库


app = FastAPI()
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

app.include_router(product.router)
app.include_router(category.router)
app.include_router(order.router)
