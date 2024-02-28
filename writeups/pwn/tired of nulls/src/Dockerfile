FROM ubuntu:18.04
RUN apt-get update && apt-get install -y gcc socat 
WORKDIR /app
COPY . . 
ENV FLAG=kxctf{3asy_p34sy_pwn_0r_n0t?}
ENTRYPOINT ["/app/start.sh"]
