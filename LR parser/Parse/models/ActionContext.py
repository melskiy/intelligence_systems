from typing import Dict, List

from pydantic import BaseModel


class ActionContext(BaseModel):
    tokens_dict: Dict
    token_list: List[str]
    tree: tuple
    new_state: int
