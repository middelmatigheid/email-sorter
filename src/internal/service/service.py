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
                raise ValueError( "Service accepts only objects inherited from BaseRegExp")
            self._category_reg_exps.append(category_reg_exp)
    
    def _prepared_text(self, text):
        
        if text is None:
            return ""
        
        text_in_lowercase = text.lower()
        prepared_text = text_in_lowercase.replace("ё","е")
        
        return prepared_text
    
    def _is_better_match(self, current_match, best_match):

        return (
            current_match["score"],
            -current_match["matched_words_count"]
        ) > (
            best_match["score"],
            -best_match["matched_words_count"]
        )
    
    def get_category(self, text):
        
        prepared_text = self._prepared_text(text)

        best_match = {"category": self.DEFAULT_CATEGORY, "score":0, "matched_words_count":0}
        
        for category_reg_exp in self._category_reg_exps:
            
            value, words_count = category_reg_exp.get_match(prepared_text)
            current_match = {"category": category_reg_exp.category,
                             "score": value,
                             "matched_words_count":words_count}

            if self._is_better_match(current_match, best_match):
                best_match = current_match

        return best_match["category"]
    
        