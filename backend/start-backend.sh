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
from sqlalchemy import create_engine, inspect, MetaData
from sqlalchemy.exc import SQLAlchemyError

DATABASE_URL = "mysql+mysqlconnector://root:123456@db:3306/lafdrue"

def column_exists(engine, table_name, column_name):
    inspector = inspect(engine)
    return column_name in [col['name'] for col in inspector.get_columns(table_name)]

try:
    engine = create_engine(DATABASE_URL)
    metadata = MetaData()
    metadata.reflect(bind=engine)

    all_columns_exist = True

    with engine.connect() as connection:
        for table in metadata.tables.values():
            for column in table.columns:
                if not column_exists(engine, table.name, column.name):
                    all_columns_exist = False
                    break
            if not all_columns_exist:
                break

        if all_columns_exist:
            print("所有列都存在，跳过迁移。")
        else:
            alembic_cfg = Config("alembic.ini")
            command.upgrade(alembic_cfg, "head")
except SQLAlchemyError as e:
    print(f"数据库错误: {e}")
    sys.exit(1)
END

# 启动 FastAPI 应用并启用热重载
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir /backend
