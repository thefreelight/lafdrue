#!/bin/bash

# 等待数据库完全启动
echo "Waiting for database to start..."
until python3 << END
import sys
import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host='db', database='lafdrue', user='root', password='123456')
    if conn.is_connected():
        print('Connected to MySQL database')
        sys.exit(0)
except Error as e:
    print(e)
    sys.exit(1)
END
do
    sleep 1
done

# 应用迁移到数据库
alembic upgrade head

# 启动 FastAPI 应用
uvicorn app.main:app --host 0.0.0.0 --port 8000
