from typing import List, Dict, Tuple

from Grammar.models import GrammarRule


class GrammarNumbering:

    def number_grammar(self, rules: List[GrammarRule]) -> Tuple[Dict[int, str], Dict[int, Dict[str, int]]]:
        raise NotImplementedError

    def _create_numbered_rhs(self, rules: List[GrammarRule]) -> Dict[int, Dict[str, int]]:
        raise NotImplementedError
