from lexer.impl.LexerImpl import LexerImpl
from consts import Consts
from states.core.State import State


class StateAER(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        LexerImpl.validate_symbol(Consts.TOKEN)
        Consts.TOKEN = LexerImpl.validate_symbol(self.s)
        nxt = Consts.STACK.pop()
        return nxt
