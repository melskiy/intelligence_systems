from typing import List, Tuple

from ElevatorSystem.Elevator import Elevator
from FiniteStateMachine.core.FiniteStateMachine import FiniteStateMachine


class ElevatorController:
    def __init__(self, total_floors: int, elevator_positions: List[int], fsm: FiniteStateMachine):
        self.fsm = fsm
        self.total_floors = total_floors
        self.elevators = [Elevator(elevator_id=i + 1, initial_floor=pos, total_floors=total_floors, fsm=self.fsm)
                          for i, pos in enumerate(elevator_positions)]
        self.calls: List[Tuple[int, int]] = []

    def add_call(self, call_floor: int, destination_floor: int):
        self.calls.append((call_floor, destination_floor))

    def assign_elevator(self, call_floor: int) -> Elevator:
        closest_elevator = min(self.elevators, key=lambda e: abs(e.current_floor - call_floor))
        return closest_elevator

    def process_calls(self):
        results = []

        for call_num, (call_floor, destination_floor) in enumerate(self.calls, start=1):
            elevator = self.assign_elevator(call_floor)
            print(
                f"\nВызов {call_num}: этаж {call_floor} -> этаж {destination_floor}. Назначен лифт {elevator.elevator_id}.")

            commands = []

            def add_movement_commands(start_floor, end_floor):
                move_commands = {(start_floor < end_floor): "move_up",
                                 (start_floor >= end_floor): "move_down"}

                move_command = move_commands[True]
                num_moves = abs(end_floor - start_floor)
                commands.extend([move_command] * num_moves)

            add_movement_commands(elevator.current_floor, call_floor)
            commands.extend(["open_doors", "close_doors", "idle"])

            add_movement_commands(call_floor, destination_floor)
            commands.extend(["open_doors", "close_doors", "idle"])

            elevator.execute_sequence(commands)

            movement_before_open = abs(elevator.current_floor - call_floor)

            results.append({
                "call_num": call_num,
                "elevator_id": elevator.elevator_id,
                "movements": movement_before_open
            })

        return results
