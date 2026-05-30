from copy import deepcopy 

from .base_service import BaseService
from ..regexp.base_regexp import BaseRegExp

class Service(BaseService):
    DEFAULT_CATEGORY = "Без категории"
    