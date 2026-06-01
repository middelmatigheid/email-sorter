import os
import yaml
from ..models.config import Config
from ..models.category import Category
from ..models.word import Word

def get_config(path, logs):
    if path.split(".")[-1] != "yaml":
        raise ValueError("Config should have .yaml extension")
    elif not os.path.exists(path):
        raise ValueError("Specified path to the config doesn't exist")
    
    with open(path, 'r', encoding='utf-8') as file:
        settings = yaml.safe_load(file)

    if "input_folder" not in settings:
        raise KeyError("Param 'input_folder' should be specified")
    else:
        input_folder = settings["input_folder"]
    
    if "output_folder" not in settings:
        raise KeyError("Param 'output_folder' should be specified")
    else:
        output_folder = settings["output_folder"]

    if "logs_level" not in settings:
        raise KeyError("Param 'logs_level' should be specified")
    else:
        logs_level = settings["logs_level"]

    if "logs_file" not in settings:
        raise KeyError("Param 'logs_file' should be specified")
    else:
        logs_file = settings["logs_file"]

    if "categories" not in settings:
        raise KeyError("Param 'categories' should be specified")
    else:
        categories = []
        for c in settings["categories"]:
            name = list(c.keys())[0]
            words = []
            for w in c[name]:
                if "word" not in w:
                    raise KeyError(f"Param 'word' in category '{name}' should be specified")
                elif "weight" not in w:
                    raise KeyError(f"Param 'weight' in category '{name}' should be specified")
                word = Word(w["word"], w["weight"])
                words.append(word)
            category = Category(name, words)
            categories.append(category)
    
    config = Config(input_folder, output_folder, logs_level, logs_file, categories)
    return config
