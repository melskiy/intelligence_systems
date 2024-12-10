from container import container

from ElevatorSystem.ElevatorController import ElevatorController
from FiniteStateMachine.FiniteStateMachineInitializer import FiniteStateMachineInitializer
from FiniteStateMachine.core.FiniteStateMachine import FiniteStateMachine


def main():
    FiniteStateMachineInitializer().initialize()
    total_floors = 10
    elevator_positions = [1, 6, 3]
    calls = [
        (4, 5),
        (9, 3),
        (2, 8),
        (6, 2)
    ]

    controller = ElevatorController(total_floors=total_floors, elevator_positions=elevator_positions,
                                    fsm=container.resolve(FiniteStateMachine))
    for call in calls:
        controller.add_call(*call)

    results = controller.process_calls()

    print("\nРезультаты вызовов:")
    for result in results:
        print(
            f"Вызов {result['call_num']}: Лифт {result['elevator_id']} совершил {result['movements']} перемещений до открытия дверей на вызове.")


if __name__ == "__main__":
    main()
