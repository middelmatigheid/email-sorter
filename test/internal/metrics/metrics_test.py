import pytest
from src.internal.metrics.metrics import Metrics  

def test_single_add_to_category():
    metrics = Metrics()
    metrics.add_to_category("category")
    assert metrics.total == 1
    assert metrics.categories["category"] == 1

def test_add_to_category_is_same():
    metrics = Metrics()
    metrics.add_to_category("category")
    metrics.add_to_category("category")
    assert metrics.total == 2
    assert metrics.categories["category"] == 2

def test_add_to_category_is_different():
    metrics = Metrics()
    metrics.add_to_category("category1")
    metrics.add_to_category("category2")
    assert metrics.total == 2
    assert metrics.categories["category1"] == 1
    assert metrics.categories["category2"] == 1