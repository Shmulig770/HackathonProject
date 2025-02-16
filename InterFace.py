from abc import ABC , abstractmethod

class KeyLoggerSystem(ABC):

    @abstractmethod
    def start_listening(self):
        pass

    @abstractmethod
    def stop_listening(self):
        pass

    @abstractmethod
    def on_press(self, key):
        pass

    @abstractmethod
    def get_logged_keys(self):
        pass