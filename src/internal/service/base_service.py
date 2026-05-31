from abc import ABC, abstractmethod

class BaseService(ABC):
    @abstractmethod
    def get_category(self, text) -> str:
        pass 