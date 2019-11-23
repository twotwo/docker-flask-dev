FROM python:3.7.4-slim-stretch

RUN sed -i s@/deb.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list && \
    sed -i s@/security.debian.org/@/mirrors.tuna.tsinghua.edu.cn/@g /etc/apt/sources.list && \
    apt-get update && apt-get install --no-install-recommends -y \
    apt-utils gcc libc-dev && \
    rm -rf /var/lib/apt/lists/* && \
    echo "[global]" > /etc/pip.conf && \
    echo "index-url = https://mirrors.aliyun.com/pypi/simple" >> /etc/pip.conf && \
    python -m pip install --upgrade pip && \
    python -m pip install --no-cache-dir pipenv

EXPOSE 8080
VOLUME /opt/flask_app/data

WORKDIR /opt/flask_app
COPY . /opt/flask_app
COPY .bashrc /root

RUN pipenv install --python 3.7 --deploy --system
CMD flask run