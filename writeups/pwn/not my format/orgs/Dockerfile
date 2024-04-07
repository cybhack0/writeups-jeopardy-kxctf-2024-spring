FROM ubuntu:18.04
RUN apt-get update && apt-get install -y gcc socat 
WORKDIR /app
COPY . . 
ENV FLAG=kxctf{f0rm4t1ng_str1ng_1s_aw3s0me_bruh_1m_pr0ud_0f_u_ma_b0y_<3}
ENTRYPOINT ["/app/start.sh"]
