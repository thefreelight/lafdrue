#!/bin/bash

# 确保数据库完全启动
echo "Waiting for database to start..."
sleep 10

# 生成新的 Alembic 迁移
alembic revision --autogenerate -m "Generated migration"

# 应用迁移到数据库
alembic upgrade head

# 启动 FastAPI 应用
uvicorn app.main:app --host 0.0.0.0 --port 8000
