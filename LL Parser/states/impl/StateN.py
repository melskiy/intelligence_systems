from lexer.impl.LexerImpl import LexerImpl
from states.core.State import State


class StateN(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        result = lambda: self.next if self.s in LexerImpl.direct_tokens else self.c + 1
        return result()
