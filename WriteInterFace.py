from abc import ABC ,abstractmethod

class IWrite(ABC):
    @abstractmethod
    def write_to_file(self, data: str):
        pass