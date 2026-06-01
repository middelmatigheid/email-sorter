import pytest
from src.internal.models.word import Word
from src.internal.models.category import Category
from src.internal.regexp.regexp import RegExp

def test_not_category():
    with pytest.raises(ValueError, match="RegExp's category should implement class Category"):
        regexp = RegExp("text")

def test_get_match():
    words = [Word("word", 1), Word("another", 2)]
    category = Category("category", words)
    regexp = RegExp(category)
    text = "dfkdofkfokekfe word ewkoekwoe another fdfdf"
    result = regexp.get_match(text)
    assert result[0] == 3
    assert result[1] == 2

def test_get_match_empty_text():
    words = [Word("word", 1), Word("another", 2)]
    category = Category("category", words)
    regexp = RegExp(category)
    text = ""
    result = regexp.get_match(text)
    assert result[0] == 0
    assert result[1] == 0

def test_get_match_uppercase():
    words = [Word("WORD", 1), Word("ANOTHER", 2)]
    category = Category("category", words)
    regexp = RegExp(category)
    text = "dfkdofkfokekfe word ewkoekwoe another fdfdf"
    result = regexp.get_match(text)
    assert result[0] == 3
    assert result[1] == 2

def test_get_match_replace():
    words = [Word("ё", 2)]
    category = Category("category", words)
    regexp = RegExp(category)
    text = "dfkdofkfokekfe е ё fdfdf"
    result = regexp.get_match(text)
    assert result[0] == 2
    assert result[1] == 1