from ..models.category import Category
from copy import deepcopy

class Config:
    def __init__(self, input_folder, output_folder, logs_file, categories):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.logs_file = logs_file
        self.categories = categories

    @property
    def categories(self):
        return deepcopy(self._categories)
    
    @categories.setter
    def categories(self, cs):
        self._categories = []
        for c in cs:
            if not isinstance(c, Category):
                raise ValueError("Config's categories should have type 'Category'")
            self._categories.append(c)
            
    def __str__(self):
        result = f"input_folder: {self.input_folder}\noutput_folder: {self.output_folder}"
        for c in self._categories:
            result += f"\n{c}"
        return result
    

    def __repr__(self):
        categories = []
        for c in self._categories:
            categories.append(repr(c))
        return f"Config('{self.input_folder}', '{self.output_folder}', [{', '.join(categories)}])"
