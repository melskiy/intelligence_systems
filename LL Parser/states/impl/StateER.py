from lexer.impl.LexerImpl import LexerImpl
from states.core.State import State
from consts import Consts


class StateER(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        LexerImpl.validate_symbol(self.s)
        nxt = Consts.STACK.pop()
        return nxt
