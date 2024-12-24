from Parse.core.ParserAction import ParserAction
from Parse.models.ActionContext import ActionContext
from Parse.models.ParseState import ParserState


class ShiftAction(ParserAction):
    def __call__(self, state: ParserState, context: ActionContext) -> None:
        state.stack_symbols.append(state.current_token)
        state.stack_states.append(context.new_state)

        token_increment = 1 if state.current_token in context.tokens_dict else 0
        state.index += token_increment
        state.current_token = context.token_list[state.index]
