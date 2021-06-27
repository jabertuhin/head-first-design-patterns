from abc import abstractmethod


class QuackBehavior:
    @abstractmethod
    def quack(self) -> None:
        pass


class Quack(QuackBehavior):
    def quack(self) -> None:
        print("Quack! Quack!! Quack!!!")


class MuteQuack(QuackBehavior):
    def quack(self) -> None:
        print("<<Pin Drop Silence>>")


class Squeak(QuackBehavior):
    def quack(self) -> None:
        print("Squeak! Squeak! Squeak!")