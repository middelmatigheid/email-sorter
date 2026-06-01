import pytest 

from src.internal.service.service import Service
from src.internal.regexp.base_regexp import BaseRegExp

class FakeRegExp(BaseRegExp):
    def __init__(self, category, score,word_count):
        self._category = category
        self._score = score
        self._word_count = word_count
    
    @property
    def category(self):
        return self._category
    def get_match(self, text):
        return self._score, self._word_count
    
def test_not_regexp():
    with pytest.raises(ValueError, match="Service accepts only objects inherited from BaseRegExp"):
        service = Service(["text"])

def test_get_category():
    regexp = FakeRegExp("category", 1,1)
    service = Service([regexp])
    assert service.get_category("") == "category"

def test_prepared_not_none_text():
    service = Service([])

    result = service._prepared_text("Ёж ёж")

    assert result == "еж еж"

def test_prepared_NoneText():
    service = Service([])

    result = service._prepared_text(None)

    assert result == ""

def test_get_category_returns_default():
    regexp = FakeRegExp("category", 0,0)

    service = Service([regexp])
    result = service.get_category("ordinary text")

    assert result == "Без категории"

def test_get_category_returns_with_best_score():

    first = FakeRegExp("first", 6,2)
    second = FakeRegExp("second", 7,3)

    service = Service([first, second])

    result = service.get_category("text")
    assert result == "second"

def test_get_category_returns_with_same_score_lower_count():

    first = FakeRegExp("first", 6,2)
    second = FakeRegExp("second", 6,3)

    service = Service([first, second])

    result = service.get_category("text")
    assert result == "first"






