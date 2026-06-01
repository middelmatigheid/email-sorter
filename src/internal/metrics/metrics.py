from .base_metrics import BaseMetrics

class Metrics(BaseMetrics):
    def __init__(self):
        self.total = 0
        self.categories = {}
    
    def get_metrics(self):
        result = f"Всего было обработано {self.total} файлов, из них:"
        for category in self.categories:
            result += f"\n- {self.categories[category]} шт."
        return result

    def add_to_category(self, category):
        self.total += 1
        self.categories[category] = self.categories.get(category, 0) + 1