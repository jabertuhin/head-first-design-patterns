from abc import abstractmethod


class FlyBehavior:
    @abstractmethod
    def fly(self) -> None:
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying with wings!")

    
class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly! :(")