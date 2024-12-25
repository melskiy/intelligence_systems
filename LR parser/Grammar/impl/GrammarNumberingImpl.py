from typing import List, Tuple, Dict

from Grammar.core import GrammarNumbering
from Grammar.models import GrammarRule


class GrammarNumberingImpl(GrammarNumbering):
    def __init__(self, starting_number: int = 11):
        self.starting_number = starting_number

    def number_grammar(self, rules: List[GrammarRule]) -> Tuple[Dict[int, str], Dict[int, Dict[str, int]]]:
        numbered_lhs = {i: rule.lhs for i, rule in enumerate(rules)}
        numbered_rhs = self._create_numbered_rhs(rules)
        return numbered_lhs, numbered_rhs

    def _create_numbered_rhs(self, rules: List[GrammarRule]) -> Dict[int, Dict[str, int]]:
        numbered_rhs = {}
        current_number = self.starting_number

        for group_index, rule in enumerate(rules):
            numbered_rhs[group_index] = {}
            for item in rule.rhs:
                numbered_rhs[group_index][item] = current_number
                current_number += 1

        return numbered_rhs
