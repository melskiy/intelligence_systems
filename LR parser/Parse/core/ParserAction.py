from Parse.models.ActionContext import ActionContext
from Parse.models.ParseState import ParserState


class ParserAction:
    def __call__(self, state: ParserState, context: ActionContext) -> None:
        raise NotImplementedError
