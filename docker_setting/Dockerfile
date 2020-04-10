FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY pip.conf /root/.pip/pip.conf
COPY . .
RUN pip install -r /usr/src/app/requirement.txt

RUN echo "make base tornado success"