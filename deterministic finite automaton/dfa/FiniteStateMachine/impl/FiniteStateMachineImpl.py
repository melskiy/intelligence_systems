from typing import Optional, Callable

from FiniteStateMachine.core.FiniteStateMachine import FiniteStateMachine


class FiniteStateMachineImpl(FiniteStateMachine):
    def __init__(self, initial_state):
        self.states = {initial_state}
        self.transitions: dict[tuple[str, str], str] = {}
        self.current_state = initial_state
        self.handlers: dict[tuple[str, str], Callable] = {}

    def add_state(self, state):
        self.states.add(state)

    def add_transition(self, from_state, command, to_state, handler: Optional[Callable] = None):
        self.transitions[(from_state, command)] = to_state
        self.handlers[(from_state, command)] = handler

    def execute_command(self, command):
        try:
            transition_key = (self.current_state, command)
            self.handlers.get(transition_key)()
            self.current_state = self.transitions[transition_key]
        except Exception as e:
            raise KeyError(f"Нет перехода из состояния '{self.current_state}' по команде '{command}'. {str(e)}")

    def get_current_state(self):
        return self.current_state

    def reset(self, initial_state):
        try:
            self.current_state = initial_state
        except Exception:
            raise ValueError(f"Состояние '{initial_state}' не добавлено в автомат.")