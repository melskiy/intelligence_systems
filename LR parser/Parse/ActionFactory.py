from typing import Optional

from Parse.core.ParserAction import ParserAction
from Parse.impl.ReduceAction import ReduceAction
from Parse.impl.ShiftAction import ShiftAction


class ActionFactory:
    @staticmethod
    def create_action(action_type: str) -> Optional[ParserAction]:
        actions = {
            's': ShiftAction(),
            'r': ReduceAction()
        }
        return actions.get(action_type)
