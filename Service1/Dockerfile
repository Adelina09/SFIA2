FROM python:alpine3.11

RUN mkdir ./opt/service1

COPY . /opt/service1

WORKDIR /opt/service1

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