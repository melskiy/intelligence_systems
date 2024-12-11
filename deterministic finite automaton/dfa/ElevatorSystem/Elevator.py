from typing import List

from FiniteStateMachine.FiniteStateMachineInitializer import FiniteStateMachineFactory


class Elevator:
    def __init__(self, elevator_id: int, initial_floor: int, total_floors: int, fsm: FiniteStateMachineFactory):
        self.movement_count = 0
        self.elevator_id = elevator_id
        self.current_floor = initial_floor
        self.total_floors = total_floors
        self.fsm = fsm()
        self._setup_fsm()

    def _setup_fsm(self):
        self.fsm.add_state("Idle")
        self.fsm.add_state("MovingUp")
        self.fsm.add_state("MovingDown")
        self.fsm.add_state("DoorsOpen")
        self.fsm.add_state("DoorsClosed")
        self.fsm.add_transition("Idle", "move_up", "MovingUp", handler=self.move_up)
        self.fsm.add_transition("Idle", "move_down", "MovingDown", handler=self.move_down)
        self.fsm.add_transition("Idle", "open_doors", "MovingUp", handler=self.open_doors)
        self.fsm.add_transition("MovingUp", "move_up", "MovingUp", handler=self.move_up)
        self.fsm.add_transition("MovingDown", "move_down", "MovingDown", handler=self.move_down)
        self.fsm.add_transition("MovingUp", "open_doors", "DoorsOpen", handler=self.open_doors)
        self.fsm.add_transition("MovingUp", "close_doors", "DoorsClosed", handler=self.close_doors)
        self.fsm.add_transition("MovingDown", "open_doors", "DoorsOpen", handler=self.open_doors)
        self.fsm.add_transition("DoorsOpen", "close_doors", "DoorsClosed", handler=self.close_doors)
        self.fsm.add_transition("DoorsClosed", "idle", "Idle", handler=self.idle)

    def bad_rule(self):
        raise Exception(f"Невозможно выполнить действие")

    def good_rule(self):
        pass

    def move_up(self):
        rules = {(self.current_floor >= self.total_floors): self.bad_rule,
                 (self.current_floor < self.total_floors): self.good_rule}

        rules[True]()

        self.current_floor += 1
        self.movement_count += 1
        print(f"Лифт {self.elevator_id} поднялся на этаж {self.current_floor}.")

    def move_down(self):
        rules = {(self.current_floor <= 1): self.bad_rule,
                 (self.current_floor > 1): self.good_rule}

        rules[True]()

        self.current_floor -= 1
        self.movement_count += 1
        print(f"Лифт {self.elevator_id} спустился на этаж {self.current_floor}.")

    def open_doors(self):
        print(f"Лифт {self.elevator_id} открыл двери на этаже {self.current_floor}.")

    def close_doors(self):
        print(f"Лифт {self.elevator_id} закрыл двери на этаже {self.current_floor}.")

    def idle(self):
        print(f"Лифт {self.elevator_id} в режиме ожидания на этаже {self.current_floor}.")

    def execute_sequence(self, commands: List[str]):
        for command in commands:
            try:
                self.fsm.execute_command(command)
            except Exception as e:
                print(f"Лифт {self.elevator_id}: Ошибка - {e}")

    def reset(self):
        self.fsm.reset("Idle")
        self.movement_count = 0
