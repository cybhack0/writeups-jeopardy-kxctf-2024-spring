FROM ubuntu:18.04
RUN apt-get update && apt-get install -y gcc socat 
WORKDIR /app
COPY . . 
ENV FLAG=kxctf{u_@r3_str0ng_0n3_but_th4ts_n0t_4ll_OxSBI}
ENTRYPOINT ["/app/start.sh"]
