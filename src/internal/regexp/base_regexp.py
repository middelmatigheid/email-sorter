from abc import ABC, abstractmethod

class BaseRegExp(ABC):
    @abstractmethod
    def get_match(self, text):
        pass