from typing import Dict


class TokenDefinitionProvider:
    @staticmethod
    def get_token_definitions() -> Dict[str, str]:
        return {
            'LPAR': r'\(',
            'RPAR': r'\)',
            'LBRACE': r'\{',
            'RBRACE': r'\}',
            'COMMA': r',',
            'SEMI': r';',
            'RETURN': r'return',
            'IF': r'if',
            'ELSE': r'else',
            'WHILE': r'while',
            'OR': r'\bor\b',
            'AND': r'\band\b',
            'TRUE': r'true',
            'FALSE': r'false',
            'ID': r'[a-zA-Z_][a-zA-Z0-9_]*',
            'NUMBER': r'[0-9]+',
            'EQ': r'==',
            'NEQ': r'!=',
            'LT': r'<',
            'GT': r'>',
            'LE': r'<=',
            'GE': r'>=',
            'PLUS': r'\+',
            'MINUS': r'-',
            'TIMES': r'\*',
            'DIVIDE': r'/',
            'NOT': r'not',
            'EPS': r'EPS'
        }
