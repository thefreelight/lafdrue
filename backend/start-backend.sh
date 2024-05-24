#!/bin/bash

# 等待数据库完全启动
echo "等待数据库启动..."
until python3 << END
import sys
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='db', database='lafdrue', user='root', password='123456')
    if conn.is_connected():
        print('已连接到MySQL数据库')
        sys.exit(0)
except Error as e:
    print(e)
    sys.exit(1)
END
do
    sleep 5  # 增加等待时间
done

# 检查并运行Alembic迁移
echo "检查并运行数据库迁移..."
python3 << END
from alembic.config import Config
from alembic import command
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "mysql+mysqlconnector://root:123456@db:3306/lafdrue"
ALEMBIC_CFG_PATH = "/backend/alembic.ini"

def check_and_upgrade():
    try:
        # 连接数据库
        engine = create_engine(DATABASE_URL)

        # 检查数据库是否已应用所有迁移
        alembic_cfg = Config(ALEMBIC_CFG_PATH)
        command.upgrade(alembic_cfg, "head")

        # 自动生成迁移脚本
        command.revision(alembic_cfg, autogenerate=True, message="Auto migration")

        # 应用新生成的迁移
        command.upgrade(alembic_cfg, "head")

    except SQLAlchemyError as e:
        print(f"数据库错误: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)

check_and_upgrade()
END

# 启动 FastAPI 应用并启用热重载
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir /backend
