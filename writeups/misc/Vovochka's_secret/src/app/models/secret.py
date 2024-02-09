from hashlib import sha256

class Secret:
    def __init__(self, name_secret, timestamp, telegram_id, secret):
        self.name_secret = name_secret
        self._telegram_id = telegram_id
        self.timestamp = timestamp
        self.secret = secret
    
    def set_logger(self, logger):
        self._logger = logger

    def log_created(self):
        self._logger.info(f"Seved new secret. Params: {self.name_secret}:{self.timestamp}")

    def get_passwd(self):
        hasher = self.name_secret + str(self._telegram_id)
        return sha256(hasher.encode()).hexdigest()

    