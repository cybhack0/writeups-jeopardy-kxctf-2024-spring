from sage.all import *

p = 0x8000000000000000000000000000000000000000000000000000000000000431
K = GF(p)
a = K(0x7)
b = K(0x5fbff498aa938ce739b8e022fbafef40563f6e6a3472fc2a514c0ce9dae23b7e)
E = EllipticCurve(K, (a, b))
Q = E(0x2, 0x8e2a8a0e65147d4bd6316030e16d19c85c97f0a9ca267122b96abbcea7e8fc8)
E.set_order(0x8000000000000000000000000000000150fe8a1892976154c59cfc193accf5b3 * 0x1)
P = E(0x2e96a1bde8aea4cdb5a550ce71eb1ddda11c92b868239c794d5542c4cadc693f, 0x21355a5b2dbd646f1b10a152ce309749fbb4b4ba82d1b1da8d02583f21c1179e)

def Gammator_X(key : bytes, n : int) -> bytes:
    inner_state = int.from_bytes(key)
    output = b''
    while len(output) < n:
        output += (int((inner_state * Q)[0]) & ((1 << 256) - 1)).to_bytes(32)[2:]
        inner_state = int((inner_state * P)[0]) & ((1 << 256) - 1)
    return output[:n]

def main():
    backdoor = 11
    pt_leak = open("first_paragraph.txt", "rb").read()
    encrypted = open("encrypted.bin", "rb").read()
    gamma_leak = bytes(x^y for x,y in zip(pt_leak, encrypted))[:30]
    for i in range(256):
        print(i)
        for j in range(256):
            x = K(int.from_bytes(bytes([i,j]) + gamma_leak))
            try:
                A = E.lift_x(x)
            except Exception:
                continue
            inner_state_1 = (int((backdoor * A)[0]) & ((1 << 256) - 1)).to_bytes(32)
            test_gamma = gamma_leak + Gammator_X(inner_state_1, 30)
            test_pt = bytes(x^y for x,y in zip(encrypted, test_gamma))
            if test_pt == pt_leak[:len(test_pt)]:
                gamma = gamma_leak + Gammator_X(inner_state_1, len(encrypted))
                pt = bytes(x^y for x,y in zip(encrypted, gamma))
                print(pt)
                exit()


if __name__ == "__main__": main()