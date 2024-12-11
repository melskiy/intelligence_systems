class FiniteStateMachine:

    def add_state(self, state):
        raise NotImplementedError

    def add_transition(self, from_state, to_state, command):
        raise NotImplementedError

    def execute_command(self, command):
        raise NotImplementedError

    def current_status(self):
        raise NotImplementedError

    def reset(self, param):
        raise NotImplementedError
