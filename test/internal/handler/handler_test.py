import os
import shutil
import pytest
from src.internal.service.base_service import BaseService
from src.internal.metrics.base_metrics import BaseMetrics
from src.internal.logger.base_logger import BaseLogger
from src.internal.handler.handler import Handler

class MockService(BaseService):
    def __init__(self):
        pass

    def get_category(self, text):
        return "category"
    
class MockMetrics(BaseMetrics):
    def __init__(self):
        pass

    def add_to_category(self, category):
        pass

    def get_metrics(self):
        pass

class MockLogger(BaseLogger):
    def __init__(self):
        pass

    def info(self, text):
        pass

    def error(self, text):
        pass

    def stats(self):
        pass

def test_not_service():
    with pytest.raises(ValueError, match="Handler's service should implement class BaseService"):
        handler = Handler("input_test", "output_test", "service", "metrics", "logger")

def test_not_metrics():
    service = MockService()
    with pytest.raises(ValueError, match="Handler's metrics should implement class BaseMetrics"):
        handler = Handler("input_test", "output_test", service, "metrics", "logger")

def test_not_logger():
    service = MockService()
    metrics = MockMetrics()
    with pytest.raises(ValueError, match="Handler's logger should implement class BaseLogger"):
        handler = Handler("input_test", "output_test", service, metrics, "logger")

def test_handle_file_doesnt_exist():
    service = MockService()
    metrics = MockMetrics()
    logger = MockLogger()
    handler = Handler("input_test", "output_test", service, metrics, logger)
    with pytest.raises(ValueError, match=f"Specified path 'input_test/unknown.txt' doesn't exist"):
        handler.handle("unknown.txt")

def test_handle_file_not_txt():
    service = MockService()
    metrics = MockMetrics()
    logger = MockLogger()
    handler = Handler("input_test", "output_test", service, metrics, logger)
    if not os.path.exists("input_test"):
        os.mkdir("input_test")
    with open("input_test/not_mail.json", "w", encoding="utf-8") as file:
        file.write("")
    if not os.path.exists("output_test"):
        os.mkdir("output_test")
    if not os.path.exists("output_test/Не письма"):
        os.mkdir("output_test/Не письма")
    handler.handle("not_mail.json")
    if not os.path.exists("output_test/Не письма/not_mail.json"):
        assert False
    shutil.rmtree("input_test")
    shutil.rmtree("output_test")

def test_handle():
    service = MockService()
    metrics = MockMetrics()
    logger = MockLogger()
    handler = Handler("input_test", "output_test", service, metrics, logger)
    if not os.path.exists("input_test"):
        os.mkdir("input_test")
    with open("input_test/mail.txt", "x", encoding="utf-8") as file:
        file.write("")
    if not os.path.exists("output_test"):
        os.mkdir("output_test")
    if not os.path.exists("output_test/category"):
        os.mkdir("output_test/category")
    handler.handle("mail.txt")
    if not os.path.exists("output_test/category/mail.txt"):
        assert False
    shutil.rmtree("input_test")
    shutil.rmtree("output_test")
