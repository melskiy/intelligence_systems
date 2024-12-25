from Grammar.core.GrammarParser import GrammarParser
from Grammar.models import GrammarRule


class GrammarParserImpl(GrammarParser):

    def __call__(self, rule: str) -> GrammarRule:
        lhs, rhs = rule.split("->")
        return GrammarRule(
            lhs=lhs.strip(),
            rhs=rhs.strip().split()
        )
