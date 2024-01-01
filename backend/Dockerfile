# backend/Dockerfile

# 使用官方 Python 镜像
FROM python:3.11

# 设置工作目录
WORKDIR /app

# 复制依赖文件并安装依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制后端代码
COPY . .

# 指定启动命令
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
