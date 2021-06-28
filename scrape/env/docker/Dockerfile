FROM ubuntu:20.04
SHELL ["/bin/bash", "-c"]
WORKDIR /root/ 
ENV DEBIAN_FRONTEND=noninteractive
ARG GECKO_VER=0.29.0
RUN \
  apt update -q=2 \
  && apt install -yq=2 \
  apt-utils \
  firefox \
  fonts-noto-cjk \
  software-properties-common \
  wget \
  && apt update -q=2 \
  && apt-add-repository ppa:deadsnakes/ppa \
  && apt update -q=2 \
  && apt install -yq=2 \
  python3.9 \
  python3.9-dev \
  python3.9-distutils \
  python3-pip \
  && ln -fns /usr/bin/python3.9 /usr/bin/python3 \
  && pip3 install -U pip \
  && wget https://github.com/mozilla/geckodriver/releases/download/v${GECKO_VER}/geckodriver-v${GECKO_VER}-linux64.tar.gz \
  && tar -C /usr/bin/ -xvzf geckodriver*.tar.gz \
  && rm geckodriver* \
  && chmod +x /usr/bin/geckodriver

COPY py/requirements.txt .
RUN \
  apt update -q=2 \
  && pip install -Ur requirements.txt \
  && rm requirements.txt