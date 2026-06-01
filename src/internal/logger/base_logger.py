from abc import ABC, abstractmethod

class BaseLogger(ABC):
    @abstractmethod
    def info(self, text):
        pass

    @abstractmethod
    def error(self, text):
        pass

    @abstractmethod
    def stats(self, text):
        pass
