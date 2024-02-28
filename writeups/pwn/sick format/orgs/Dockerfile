FROM ubuntu:18.04
RUN apt-get update && apt-get install -y gcc socat 
WORKDIR /app
COPY . . 
ENV FLAG=kxctf{f0rm4t1ng_str1ng_1s_c00l_d0nt_u_4gr33_w1th_m3_bruh?}
ENTRYPOINT ["/app/start.sh"]
