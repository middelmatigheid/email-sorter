class Word:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    @property
    def weight(self):
        return self._weight
        
    @weight.setter
    def weight(self, w):
        if w <= 0:
            raise ValueError("Word's weight can't be negative")
        self._weight = w

    def __str__(self):
        return f"{self.name} - {self.weight}"
    
    def __repr__(self):
        return f"Word('{self.name}', {self.weight})"
