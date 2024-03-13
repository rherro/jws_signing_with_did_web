FROM ubuntu:24.04

ENV DEBIAN_FRONTEND="noninteractive" TZ="UTC"
SHELL ["/bin/bash", "-c"]
EXPOSE 8000

RUN apt update -y && \
    apt upgrade -y

# Install Python
RUN apt install -y python3.12 && \
    apt install -y python3-pip && \
    apt install -y python3.12-venv

# Copy source
COPY . /jws_signing_with_did_web

# Setup environment
RUN cd /jws_signing_with_did_web && \
    rm -rf .venv && \
    python3 -m venv .venv && \
    source .venv/bin/activate && \
    pip install -r requirements.txt && \
    python src/django_web_server/manage.py migrate

WORKDIR /jws_signing_with_did_web
