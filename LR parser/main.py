from Grammar.GrammarTreeBuilder import GrammarTreeBuilder
from Grammar.impl.GrammarFileReaderImpl import GrammarFileReaderImpl
from Grammar.impl.GrammarNumberingImpl import GrammarNumberingImpl
from Grammar.impl.GrammarParser import GrammarParserImpl
from Lexer.LexerFactory import LexerFactory
from Lexer.provider import TokenDefinitionProvider
from Parse.ActionManager import ActionManager
import pandas as pd

tree_builder = GrammarTreeBuilder(
    file_reader=GrammarFileReaderImpl(),
    parser=GrammarParserImpl(),
    numbering=GrammarNumberingImpl(starting_number=11)
)
lexer = LexerFactory.create_lexer("func ( a ) ;")
new_df = pd.read_csv('lr1_table.csv')
grammar_tree = tree_builder.build_tree("C:/Users/User/Desktop/intelligence_systems/LR parser/rules.txt")
token_list = lexer.tokenize()
state = new_df[token_list[0]][0]
curr_action, curr_state = state[0], int(state[1:])

action_manager = ActionManager(TokenDefinitionProvider.get_token_definitions())
action_manager.execute_action(curr_action, curr_state, token_list, grammar_tree)

while action_manager.parser_state.current_token != "S'":
    curr_state = action_manager.current_state
    state = new_df[action_manager.parser_state.current_token][curr_state]
    curr_action, curr_state = state[0], int(state[1:])
    print(curr_action, curr_state)
    action_manager.execute_action(curr_action, curr_state, token_list, grammar_tree)
