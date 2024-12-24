from typing import List

from Lexer.core import TokenRepository


class TokenRepositoryImpl(TokenRepository):
    def __init__(self):
        self._tokens: List[str] = []

    def get_tokens(self) -> List[str]:
        return self._tokens

    def add_token(self, token: str) -> None:
        self._tokens.append(token)
