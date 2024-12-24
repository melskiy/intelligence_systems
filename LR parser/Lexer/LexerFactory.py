from Lexer.core import Lexer
from Lexer.impl import LexerImpl, TokenRepositoryImpl


class LexerFactory:
    @staticmethod
    def create_lexer(input_text: str) -> Lexer:
        token_repository = TokenRepositoryImpl()
        return LexerImpl(input_text, token_repository)
