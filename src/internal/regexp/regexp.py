import re
from .base_regexp import BaseRegExp
from ..models.category import Category

class RegExp(BaseRegExp):
    def __init__(self, category):
        if not isinstance(category, Category):
            raise ValueError("RegExp's category should implement class Category")
        self.category = category.name
        self.words = category.words
        for w in self.words:
            w.name = w.name.lower().replace("ё", "е")

    def get_match(self, text):
        value = 0
        words = 0
        for w in self.words:
            cur = len(re.findall(rf"{w.name}", text))
            value += cur * w.weight
            words += cur
        return value, words