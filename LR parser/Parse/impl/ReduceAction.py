from Parse.core.ParserAction import ParserAction
from Parse.models.ActionContext import ActionContext
from Parse.models.ParseState import ParserState


class ReduceAction(ParserAction):
    def __init__(self):
        self.__operations = {
            True: self._remove_elements,
            False: self._clear_stacks
        }

    def _remove_elements(self, state, elements_to_remove):
        state.stack_symbols = state.stack_symbols[:-elements_to_remove]
        state.stack_states = state.stack_states[:-elements_to_remove]
        return state

    def _clear_stacks(self, state, elements_to_remove):
        state.stack_symbols.clear()
        state.stack_states.clear()
        return state

    def __call__(self, state: ParserState, context: ActionContext) -> None:
        is_epsilon = list(context.tree[1][context.new_state].keys())[0] == ''
        elements_to_remove = 0 if is_epsilon else len(context.tree[1][context.new_state])

        operation = self.__operations[elements_to_remove is not None]
        state = operation(state, elements_to_remove)
        state.current_token = context.tree[0][context.new_state]