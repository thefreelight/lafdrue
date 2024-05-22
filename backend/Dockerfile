# 使用官方 Python 运行时作为父镜像
FROM python:3.11

# 将工作目录设置为 /backend
WORKDIR /backend

# 将当前目录内容复制到位于 /backend 的容器中
COPY . /backend

# 安装 requirements.txt 中的所有依赖
RUN pip install -r requirements.txt

# 安装其他依赖
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libmariadb-dev && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 安装 watchfiles 以支持热重载
RUN pip install watchfiles

# 复制启动脚本并赋予执行权限
COPY start-backend.sh /backend/start-backend.sh
RUN chmod +x /backend/start-backend.sh

# 暴露端口 8000 供外部访问
EXPOSE 8000

# 定义环境变量
ENV PYTHONUNBUFFERED 1

# 使用启动脚本作为容器启动命令
CMD ["/backend/start-backend.sh"]
