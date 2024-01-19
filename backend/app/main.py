# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .dependencies.database import engine, Base


from .routes import product

Base.metadata.create_all(bind=engine)  #创建数据库


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有源
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

app.include_router(product.router)
