from lexer.impl.LexerImpl import LexerImpl
from consts import Consts
from states.core.State import State


class StateNSE(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        Consts.STACK.append(self.c + 1)
        LexerImpl.validate_symbol(self.s)
        return self.next
