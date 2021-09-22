from .Strategy import Strategy
from .Student import Student


class Starosta(Student):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.doppole = "doppole"

    def outputinfo(self):
        self.strategy.outputinfo(self)

    def inputargument(self):
        self.strategy.inputargument(self)

    def __str__(self):
        return "Имя: {} \t Группа: {} \t Допполе: {}".format(self.name, self.group, self.doppole)
