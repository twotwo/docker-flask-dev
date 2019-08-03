FROM python:3.7-alpine as base
FROM base as builder
# Install Packages
# https://www.elastic.co/guide/en/beats/filebeat/7.2/filebeat-installation.html
RUN mkdir /install
WORKDIR /install
COPY requirements.txt /requirements.txt
RUN pip install --install-option="--prefix=/install"  -r /requirements.txt
FROM base
# Copy Builder Image
COPY --from=builder /install /usr/local
# Need by filebeat
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories  && \
        apk add --update --no-cache libc6-compat tzdata &&\
        ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
# Add alias
ENV ENV="/root/.ashrc"
RUN echo "alias ll='ls -l'" > "$ENV"

# COPY supervisord.conf /etc/
COPY main.py app/ /

WORKDIR /
# Set Running Env by -e RABBITMQ_HOST=xxx ...

CMD ["supervisord", "--configuration", "/etc/supervisord.conf"]

