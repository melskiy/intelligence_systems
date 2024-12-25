from typing import Dict, List

from Parse.ActionFactory import ActionFactory
from Parse.models.ActionContext import ActionContext
from Parse.models.ParseState import ParserState


class ActionManager:
    def __init__(self, tokens_dict: Dict):
        self.tokens_dict = tokens_dict
        self.action_factory = ActionFactory()
        self.parser_state = ParserState()

    def execute_action(self, action_type: str, new_state: int,
                       token_list: List[str], tree: tuple) -> None:
        action = self.action_factory.create_action(action_type)

        context = ActionContext(
            tokens_dict=self.tokens_dict,
            token_list=token_list,
            tree=tree,
            new_state=new_state
        )

        action(self.parser_state, context)

    @property
    def current_state(self) -> int:
        return self.parser_state.stack_states[-1] if self.parser_state.stack_states else 0
