import os
import shutil
from .base_handler import BaseHandler
from ..service.base_service import BaseService
from ..metrics.base_metrics import BaseMetrics
from ..logger.base_logger import BaseLogger

class Handler(BaseHandler):
    def __init__(self, input_folder, output_folder, service, metrics, logger=None):
        if not isinstance(service, BaseService):
            raise ValueError("Handler's service should implement class BaseService")
        if not isinstance(metrics, BaseMetrics):
            raise ValueError("Handler's metrics should implement class BaseMetrics")
        if not isinstance(logger, BaseLogger):
            raise ValueError("Handler's logger should implement class BaseLogger")
        self.input_folder = input_folder
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.service = service
        self.metrics = metrics
        self.logger = logger

    def handle(self, file_name):
        if not os.path.exists(f"{self.input_folder}/{file_name}"):
            if self.logger:
                self.logger.error(f"File '{file_name}' doesn't exist")
            raise ValueError(f"Specified path '{self.input_folder}/{file_name}' doesn't exist")
        
        if file_name.split(".")[-1] != "txt":
            if self.logger:
                self.logger.error(f"File '{file_name}' is not an email")
            self.metrics.add_to_category("Не письма")
            shutil.move(f"{self.input_folder}/{file_name}", f"{self.output_folder}/Не письма/{file_name}")
            return
        
        with open(f"{self.input_folder}/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
            category = self.service.get_category(text)
        if self.logger:
            self.logger.info(f"File '{file_name}' moved to category '{category}'")
        self.metrics.add_to_category(category)
        shutil.move(f"{self.input_folder}/{file_name}", f"{self.output_folder}/{category}/{file_name}")