from datetime import datetime
from .base_logger import BaseLogger

class Logger(BaseLogger):
    def __init__(self, level, file):
        if level == "info":
            self.level = 0
        elif level == "error":
            self.level = 1
        elif level != None:
            raise ValueError(f"Logger have only 'info' and 'error' levels, but '{level}' was provided")
        else:
            self.level = 2
        if file is not None and file.split(".")[-1] != "txt":
            raise ValueError("Param 'logs_file' should have .txt file")
        self.file = file

    def info(self, text):
        if self.level <= 0:
            message = f"INFO ({datetime.now()}): {text}"
            if self.file:
                with open(self.file, "a", encoding="utf-8") as file:
                    file.write(message)
            print(message)

    def error(self, text):
        if self.level <= 1:
            message = f"ERROR ({datetime.now()}): {text}"
            if self.file:
                with open(self.file, "a", encoding="utf-8") as file:
                    file.write(message)
            print(message)

    def stats(self, text):
        message = f"\n{'=' * 20}\n\nSTATS ({datetime.now()})\n{text}\n\n{'=' * 20}\n"
        if self.file:
            with open(self.file, "a", encoding="utf-8") as file:
                file.write(message)
        print(message)
