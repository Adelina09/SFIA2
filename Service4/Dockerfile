FROM python:alpine3.11

RUN mkdir ./opt/service4

COPY . /opt/service4

WORKDIR /opt/service4

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
        gcc \
        libc-dev \
        linux-headers \
        mariadb-dev \
        python3-dev \
        postgresql-dev \
    ;

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
