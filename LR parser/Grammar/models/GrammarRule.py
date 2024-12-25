from typing import List

from pydantic import BaseModel


class GrammarRule(BaseModel):
    lhs: str
    rhs: List[str]
