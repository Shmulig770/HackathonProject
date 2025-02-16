from cryptography.fernet import Fernet

class Cipher:

    def __init__(self):
        self.key = Fernet.generate_key()

    def cipher(self, data):
        code = data.encode()
        curr_key = Fernet(self.key)
        return curr_key.encrypt(code)

    def get_key(self):
        return self.key

