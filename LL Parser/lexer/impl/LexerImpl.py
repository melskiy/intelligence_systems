import re

from TokenDefinitionProvider import TokenDefinitionProvider
from consts import Consts
from lexer.core import Lexer


class LexerImpl(Lexer):
    direct_tokens = list()
    current_symbol = ''
    token_list = list()

    def __init__(self, direct_tokens, current_symbol):
        self.direct_tokens = direct_tokens
        self.current_symbol = current_symbol
        self.token_list = self.get_tokens()
        self.token_definitions = TokenDefinitionProvider.get_token_definitions()

    def tokenize(self):
        self.current_symbol = re.sub(r'\s+', '', self.current_symbol)  # Remove whitespace
        token_pattern = '|'.join(f'(?P<{key}>{value})' for key, value in self.token_definitions.items())
        matches_found = False
        position = 0
        while position < len(self.current_symbol):
            remaining_symbol = self.current_symbol[position:]
            match = re.match(token_pattern, remaining_symbol)
            try:
                matches_found = True
                token_type = match.lastgroup
                token_value = match.group()
                self.token_list.append(token_type)
                position += len(token_value)

            except:
                raise ValueError(
                    f"Error: No token found in string. Unprocessed symbol: '{self.current_symbol[position]}'"
                )

        self.token_list.append('END')
        return LexerImpl.token_list

    def get_tokens(self):
        return self.token_list

    def add_index(self):
        Consts.INDEX += 1
        return self.token_list[Consts.INDEX]

    def skip_index(self):
        return None

    @staticmethod
    def get_next_token(self):
        rule = {
            Consts.INDEX < len(self.token_list): self.add_index,
            Consts.INDEX >= len(self.token_list): self.skip_index
        }
        return rule[True]

    @staticmethod
    def validate_symbol(symbol):
        def raise_syntax_error(symbol):
            raise SyntaxError(f"Symbol '{symbol}' not found in allowed list.")

        is_valid = lambda: (symbol in LexerImpl.direct_tokens) or raise_syntax_error(symbol)
        is_valid()
