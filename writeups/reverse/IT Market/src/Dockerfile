FROM ubuntu

RUN apt-get update
RUN apt-get install -y socat
RUN mkdir /app

WORKDIR /app

COPY main /app
COPY entrypoint.sh /app


RUN chmod 555 /app/entrypoint.sh
 
ENTRYPOINT sh entrypoint.sh