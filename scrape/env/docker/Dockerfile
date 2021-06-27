# FROM python:3.9.5-alpine
# SHELL ["ash", "-c"]
# RUN apk add build-base


FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]
WORKDIR /root/ 
ENV DEBIAN_FRONTEND=noninteractive

RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  software-properties-common \
  && apt update -q=2 \
  && apt-add-repository ppa:deadsnakes/ppa \
  && apt update -q=2 \
  && apt install -yq=2 \
  python3.9 \
  python3.9-dev \
  python3.9-distutils \
  python3-pip \
  && ln -fns /usr/bin/python3.9 /usr/bin/python3 \
  && pip3 install -U pip 


COPY py/requirements.txt .
RUN \
  apt update -q=2 \
  && pip install -Ur requirements.txt \
  && rm requirements.txt