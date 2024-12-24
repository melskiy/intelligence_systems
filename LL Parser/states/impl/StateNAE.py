from lexer.impl.LexerImpl import LexerImpl
from states.core.State import State
from consts import Consts


class StateNAE(State):
    def __init__(self, curr, next, symbol):
        self.c = curr
        self.s = symbol
        self.next = next

    def transition(self):
        LexerImpl.validate_symbol(Consts.TOKEN)
        Consts.TOKEN = LexerImpl.get_next_token(self.s)
        return self.next
