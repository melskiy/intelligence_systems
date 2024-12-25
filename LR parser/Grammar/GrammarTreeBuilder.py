from typing import Tuple, Dict

from Grammar.core import GrammarFileReader, GrammarParser, GrammarNumbering


class GrammarTreeBuilder:
    def __init__(self, file_reader: GrammarFileReader, parser: GrammarParser, numbering: GrammarNumbering):
        self.file_reader = file_reader
        self.parser = parser
        self.numbering = numbering

    def build_tree(self, filename: str) -> Tuple[Dict[int, str], Dict[int, Dict[str, int]]]:
        grammar_lines = self.file_reader(filename)
        grammar_rules = [self.parser(rule) for rule in grammar_lines]
        return self.numbering.number_grammar(grammar_rules)
