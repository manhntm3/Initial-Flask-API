FROM ubuntu:18.04 

MAINTAINER Manh Nguyen "manh.ntm3@gmail.com"

RUN apt-get update -y \
    && apt-get install -y \
    gunicorn \
    python3-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY . /flask-api

WORKDIR /flask-api

RUN chmod +x prepare_server.sh

RUN pip3 install -r requirements.txt

RUN ./prepare_server.sh

CMD ["gunicorn", "--workers=4", "--worker-class=gthread","-b 0.0.0.0:9000", "wsgi:app", "--log-level=debug", "--log-file=log/logger.log"]

EXPOSE 9000
