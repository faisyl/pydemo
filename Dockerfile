FROM alpine:3.6
MAINTAINER Faisal <faisal.is@gmail.com>

# basic flask environment
RUN apk --update upgrade && apk add bash py2-openssl py2-pip py2-certifi &&\
	pip install cherrypy &&\
	mkdir /certs &&\
	rm -rf /var/cache/apk/*

ENV STACK=undefined
EXPOSE 5000

ADD app.py /
WORKDIR /

# exectute start up script
CMD ["python", "./app.py"]
