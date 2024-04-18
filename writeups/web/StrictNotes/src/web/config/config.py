import json

class Config():
    def __init__(self):
        secretsfile = json.loads(open("secrets.json").read())
        self.session_key = secretsfile['SESSION_KEY']
        self.nonce_secret = secretsfile['NONCE_SECRET']
        self.csp_config = "script-src 'nonce-{}' 'strict-dynamic'; img-src 'none'; style-src 'self'; frame-src 'none';"
