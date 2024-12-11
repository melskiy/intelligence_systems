from container import container

from FiniteStateMachine.core.FiniteStateMachine import FiniteStateMachine
from FiniteStateMachine.impl.FiniteStateMachineImpl import FiniteStateMachineImpl


class FiniteStateMachineFactory:
    def __call__(self):
        return FiniteStateMachineImpl("Idle")


class FiniteStateMachineInitializer:

    def initialize(self):
        container.register(FiniteStateMachine, FiniteStateMachineFactory)
