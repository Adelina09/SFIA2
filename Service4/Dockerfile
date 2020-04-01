FROM python:alpine3.11

RUN mkdir /opt/SFIA2/

COPY . /opt/SFIA2/

WORKDIR /opt/SFIA2/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
