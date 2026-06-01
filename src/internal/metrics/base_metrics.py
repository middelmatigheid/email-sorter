from abc import ABC, abstractmethod

class BaseMetrics(ABC):
    @abstractmethod
    def get_metrics(self):
        pass
    
    @abstractmethod
    def add_to_category(self, category):
        pass