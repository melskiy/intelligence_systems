
from consts import Consts
from lexer.impl.LexerImpl import LexerImpl
from states.impl.StateAER import StateAER
from states.impl.StateAR import StateAR
from states.impl.StateER import StateER
from states.impl.StateN import StateN
from states.impl.StateNAE import StateNAE
from states.impl.StateNE import StateNE
from states.impl.StateNSE import StateNSE

Consts.TOKEN = None
Consts.INDEX = 0
Consts.STACK = []
transitions = Consts.TRANSITIONS
state_classes = [StateNE, StateNSE, StateNAE, StateN, StateER, StateAER, StateAR]
lexer = LexerImpl(transitions[1][0], "9+9")
lexer.tokenize()
token_list = lexer.get_tokens()
Consts.TOKEN = token_list[0]
initial_state = state_classes[transitions[1][-1]](1, transitions[1][1], Consts.TOKEN)
current_state = initial_state
while Consts.TOKEN != 'END':
    current_state = current_state.transition()
    LexerImpl(transitions[current_state][0],Consts.TOKEN)
    current_state = state_classes[transitions[current_state][-1]](current_state, transitions[current_state][1], Consts.TOKEN)
