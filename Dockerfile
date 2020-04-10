FROM python36base_tornado:latest

RUN mkdir -p /usr/src/app
RUN mkdir -p /var/log/supervisor
WORKDIR /usr/src/app
COPY . /usr/src/app
CMD python /usr/src/app/main.py