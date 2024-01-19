# 使用官方 Python 运行时作为父镜像
FROM python:3.11

# 将工作目录设置为 /backend
WORKDIR /backend

# 将当前目录内容复制到位于 /backend 的容器中
COPY . /backend

# 安装 requirements.txt 中的所有依赖
RUN pip install -r requirements.txt

# 暴露端口 8000 供外部访问
EXPOSE 8000

# 定义环境变量
ENV PYTHONUNBUFFERED 1

# 运行 main.py 时启动应用
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
