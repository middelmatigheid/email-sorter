from .base_metrics import BaseMetrics

class Metrics(BaseMetrics):
    def __init__(self):
        self.total = 0
        self.categories = {}

    def add_to_category(self, category):
        self.total += 1
        self.categories[category] = self.categories.get(category, 0) + 1

    def get_metrics(self):
        if self.total == 0:
            return f"Всего было обработано {self.total} файлов"
        result = f"Всего было обработано {self.total} файлов, из них"
        for c in self.categories:
            result += f"\n - {c}: {self.categories[c]} шт"
        return result
