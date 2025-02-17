# 使用官方的 Python 基础镜像
FROM python:3.12-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录内容到工作目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r req.txt

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=11434

# 暴露端口
EXPOSE 11434

# 运行 Flask 应用
CMD ["flask", "run"]