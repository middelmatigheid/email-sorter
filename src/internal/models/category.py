from ..models.word import Word
from copy import deepcopy

class Category:
    def __init__(self, name, words):
        self.name = name
        self.words = words

    @property
    def words(self):
        return deepcopy(self._words)
    
    @words.setter
    def words(self, ws):
        self._words = []
        for w in ws:
            if not isinstance(w, Word):
                raise ValueError("Category's words should have type Word")
            self._words.append(deepcopy(w))

    def __str__(self):
        result = f"{self.name}:"
        for w in self._words:
            result += f"\n - {w}"
        return result
    
    def __repr__(self):
        words = []
        for w in self._words:
            words.append(repr(w))
        return f"Category('{self.name}', [{', '.join(words)}])"
    