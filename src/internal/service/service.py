from copy import deepcopy 

from .base_service import BaseService
from ..regexp.base_regexp import BaseRegExp

class Service(BaseService):
    DEFAULT_CATEGORY = "Без категории"

    def __init__(self, category_reg_exps):
        self.category_reg_exps = category_reg_exps

    @property
    def category_reg_exps(self):
        return self._category_reg_exps