from abc import abstractmethod

from fly_behavior import FlyBehavior, FlyWithWings
from quack_behavior import QuackBehavior, Quack


class Duck:    
    def __init__(self, fly_behavior: FlyBehavior, quack_behavior: QuackBehavior) -> None:
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior

    def perform_fly(self) -> None:
        self.fly_behavior.fly()

    def perform_quack(self) -> None:
        self.quack_behavior.quack()

    def swim(self) -> None:
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self) -> None:        
        pass    


class MallarDuck(Duck):
    def __init__(self) -> None:
        fly_behavior = FlyWithWings()
        quack_behavior = Quack()
        super().__init__(fly_behavior, quack_behavior)

    def display(self) -> None:
        print("I'm a beautiful MallarDuck.")