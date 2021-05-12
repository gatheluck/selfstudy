FROM python:3.8-slim
ENV PYTHONBUFFERED 1

RUN apt update && apt install --no-install-recommends -y \
	curl git ssh docker.io \
	&& pip3 install docker-compose

# RUN useradd -ms /bin/sh python_user
# RUN gpasswd -a python_user sudo
# USER python_user