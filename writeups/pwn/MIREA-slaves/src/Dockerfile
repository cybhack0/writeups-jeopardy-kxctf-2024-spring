FROM ubuntu:24.04

RUN apt-get update
RUN apt-get install -y socat libc6

WORKDIR /app

COPY main .
COPY entrypoint.sh .

RUN chmod +x main
RUN chmod 555 entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]
