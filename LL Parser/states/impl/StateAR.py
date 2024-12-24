from lexer.impl.LexerImpl import LexerImpl
from consts import Consts
from states.core.State import State


class StateAR(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        LexerImpl.get_next_token(self.s)
        nxt = Consts.STACK.pop()
        return nxt
