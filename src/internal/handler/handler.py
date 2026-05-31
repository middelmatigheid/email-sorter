import os
import shutil
from .base_handler import BaseHandler
from ..service.base_service import BaseService

class Handler(BaseHandler):
    def __init__(self, input_folder, output_folder, service, metrics):
        if not isinstance(service, BaseService):
            raise ValueError("Handler's service should implement class BaseService")
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.service = service
        self.metrics = metrics

    def handle(self, file_name):
        if file_name.split(".")[-1] != "txt":
            self.metrics.add_to_category("Не письма")
            shutil.move(f"{self.input_folder}/{file_name}", f"{self.output_folder}/Не письма/{file_name}")
            return

        if not os.path.exists(f"{self.input_folder}/{file_name}"):
            raise ValueError(f"Specified path '{self.input_folder}/{file_name}' doesn't exist")
        
        with open(f"{self.input_folder}/{file_name}", "r", encoding="utf-8") as file:
            text = file.read()
            category = self.service.get_category(text)
        self.metrics.add_to_category(category)
        shutil.move(f"{self.input_folder}/{file_name}", f"{self.output_folder}/{category}/{file_name}")