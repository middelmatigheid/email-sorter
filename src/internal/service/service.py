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
    
    @category_reg_exps.setter
    def category_reg_exps(self, category_reg_exps):
        self._category_reg_exps = []

        for category_reg_exp in category_reg_exps:
            if not isinstance(category_reg_exp, BaseRegExp):
                raise ValueError( "Service accepts only objects inherited from BaseGerExp")
            self._category_reg_exps.append(category_reg_exp)