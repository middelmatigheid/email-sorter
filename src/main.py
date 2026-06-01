import os
import sys
import time
from internal.config.config import get_config
from internal.regexp.regexp import RegExp
from internal.service.service import Service
from internal.metrics.metrics import Metrics
from internal.logger.logger import Logger
from internal.handler.handler import Handler

loop = False
if "--loop" in sys.argv:
    loop = True
logs = False
if "--logs" in sys.argv:
    logs = True

config = get_config("config.yaml", logs)
if not os.path.exists(f"{config.output_folder}"):
    os.mkdir(f"{config.output_folder}")
if not os.path.exists(f"{config.output_folder}/Не письма"):
    os.mkdir(f"{config.output_folder}/Не письма")
if not os.path.exists(f"{config.output_folder}/Без категории"):
    os.mkdir(f"{config.output_folder}/Без категории")

reg_exps = []
for c in config.categories:
    if not os.path.exists(f"{config.output_folder}/{c.name}"):
        os.mkdir(f"{config.output_folder}/{c.name}")
    reg_exps.append(RegExp(c))
service = Service(reg_exps)
metrics = Metrics()
logger = Logger(config.logs_level if logs else None, config.logs_file if logs else None)
handler = Handler(config.input_folder, config.output_folder, service, metrics, logger)

try:
    while True:
        inbox = os.listdir(config.input_folder)
        for file in inbox:
            handler.handle(file)
        if loop:
            time.sleep(1)
        else:
            break
except KeyboardInterrupt:
    pass

logger.stats(metrics.get_metrics())
