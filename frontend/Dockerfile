# 使用 Node.js 官方镜像
FROM node:14

# 设置工作目录
WORKDIR /app

# 复制 package.json 和 package-lock.json
COPY package*.json /app/

# 安装依赖
RUN npm install

# 复制前端源代码
COPY . /app

# 构建应用
RUN npm run build

# 安装 serve 用于运行构建的应用
RUN npm install -g serve

# 暴露端口
EXPOSE 8080

# 定义环境变量
ENV NODE_ENV=production

# 运行应用
CMD ["serve", "-s", "dist", "-l", "8080"]
