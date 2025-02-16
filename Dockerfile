# ubuntu
FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8

ADD sources.list /etc/apt/sources.list

RUN sed -i 's@http://archive.ubuntu.com/ubuntu/@http://mirrors.aliyun.com/ubuntu/@g' /etc/apt/sources.list
USER root

RUN mkdir -p /workspace
WORKDIR /workspace

ADD ./requirements.txt ./requirements.txt

RUN apt-get update && \
    apt-get install -y ca-certificates && \
    update-ca-certificates

RUN apt-get update && \
    apt-get install -y \
         libmysqlclient-dev tzdata \
         python3 python3-dev python3-pip \
         libpcre3 libpcre3-dev uwsgi-plugin-python3 \
         wget curl vim nginx

RUN pip3 install -r ./requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

ADD docker/entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
