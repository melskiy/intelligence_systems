import re
from typing import List, Optional

from Lexer.core import Lexer, TokenRepository
from Lexer.exception import LexerError
from Lexer.provider import TokenDefinitionProvider


class ValidTokenHandler:
    def handle_token(self, kind: str, repository: TokenRepository) -> None:
        repository.add_token(kind)


class NullTokenHandler:
    def handle_token(self, kind: str, repository: TokenRepository) -> None:
        pass


class TokenHandlerFactory:
    @staticmethod
    def create_handler(kind: Optional[str]):
        handlers = {
            str: ValidTokenHandler,
            None: NullTokenHandler
        }

        return handlers[type(kind)]()


class LexerImpl(Lexer):
    def __init__(self, input_text: str, token_repository: TokenRepository):
        self._input_text = input_text
        self._token_repository = token_repository
        self._token_definitions = TokenDefinitionProvider.get_token_definitions()

    def _prepare_input(self) -> str:
        return re.sub(r'\s+', '', self._input_text)

    def _create_regex_pattern(self) -> str:
        return '|'.join(f'(?P<{key}>{value})' for key, value in self._token_definitions.items())

    def tokenize(self) -> List[str]:
        cleaned_input = self._prepare_input()
        token_regex = self._create_regex_pattern()
        position = 0

        while position < len(cleaned_input):
            current_text = cleaned_input[position:]
            match = re.match(token_regex, current_text)

            try:
                kind = match.lastgroup
                value = match.group()

                handler = TokenHandlerFactory.create_handler(kind)
                handler.handle_token(kind, self._token_repository)

                position += len(value)
            except Exception:
                raise LexerError(f"Ошибка: неопознанный символ '{cleaned_input[position]}'")

        self._token_repository.add_token('$')
        return self._token_repository.get_tokens()
