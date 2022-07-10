FROM python:3-alpine
LABEL maintainer="gta98 <me@glub.xyz>"

RUN pip3 install flask

COPY ./app.py /root/app.py

RUN mkdir -p /root/logs
RUN mkdir -p /root/zips
WORKDIR /root/
ENTRYPOINT python3 app.py
