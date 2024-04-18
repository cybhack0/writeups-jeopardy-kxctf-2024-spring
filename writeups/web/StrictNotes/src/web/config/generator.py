import json, random

ALPH = [chr(i) for i in range(65, 65 + 26)]

def gen_secret() -> str:
    secret = ""
    for _ in range(16):
        secret += ALPH[random.randint(0,25)]

    return secret

secrets = dict()
secrets['SESSION_KEY'] = gen_secret()
secrets['NONCE_SECRET'] = gen_secret()

with open('secrets.json', 'w', encoding='utf-8') as file:
    json.dump(secrets, file, ensure_ascii=False, indent=4)