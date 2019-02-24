FROM python:3.7.2

# 创建容器运行时的组 flaskgroup 和用户 flaskuser
RUN groupadd flaskgroup && useradd -m -g flaskgroup -s /bin/bash flaskuser

# 创建目录并指定工作目录
RUN mkdir -p /home/flask/web
WORKDIR /home/flask/web

# 使用 requirements 安装 python 依赖，需要明确版本号以获得一致性
COPY requirements.txt /home/flask/web
RUN pip install --no-cache-dir -r requirements.txt

# 复制当前目录至容器目录
COPY . /home/flask/web

# 权限配置
RUN chown -R flaskuser:flaskgroup /home/flask
# ADD --chown=flaskuser:flaskgroup files* /home/flask

CMD ["python", "run.py"]
# CMD ["sh", "ls -a"]
# CMD echo $PWD && ls -a && cd volume && ls -a
# CMD cd volume && ls -a

USER flaskuser
# EXPOSE 5000
