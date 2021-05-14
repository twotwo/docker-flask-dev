FROM python:3.7.4-slim-stretch

WORKDIR /app

RUN sed -i s@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list && \
    sed -i s@/security.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y \
    apt-utils gcc libc-dev && \
    rm -rf /var/lib/apt/lists/* && \
    echo "[global]" > /etc/pip.conf && \
    echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> /etc/pip.conf && \
    python -m pip install --upgrade pip

EXPOSE 8080
VOLUME /opt/flask_app/data

COPY . /app
COPY .bashrc /root

RUN python -m pip install --no-cache-dir -r /app/requirements.txt

CMD [ "gunicorn", "--config", "gunicorn.conf", "app:app" ]