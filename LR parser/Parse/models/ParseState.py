from typing import List, Self

from pydantic import BaseModel


class ParserState(BaseModel):
    stack_symbols: List[str] = []
    stack_states: List[int] = []
    current_token: str = ''
    index: int = 0

