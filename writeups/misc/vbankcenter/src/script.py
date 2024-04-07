import random
import base64

string = input("Введите строку: ")
ascii_codes = []
for char in string:
    ascii_code = ord(char)
    random_number = random.randint(1000, 1337)
    rand_way = random.randint(1,2)
    if(rand_way == 1):
        diff = "chr(\""+base64.b64encode(str(random_number).encode("utf-8")).decode("utf-8")+"\"-"+str(random_number-ascii_code)+")&"
    else:   
        diff = "chr(\""+base64.b64encode(str(ascii_code-random_number).encode("utf-8")).decode("utf-8")+"\"+"+str(random_number)+")&"
    ascii_codes.append(diff)
print("Execute(",*ascii_codes,")")
