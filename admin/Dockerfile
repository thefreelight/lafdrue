# 使用 Node.js 最新稳定版本镜像
FROM node:20

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 yarn.lock 或 package-lock.json
COPY package.json yarn.lock ./

# 安装依赖
RUN yarn


# 复制前端项目代码
COPY . .

# 暴露 Vite 默认端口，通常是 3000
EXPOSE 3000

# 启动开发服务器
CMD ["yarn", "dev"]
