from .Strategy import Strategy
from .Student import Student


class Starosta(Student):
    def __init__(self, strategy: Strategy):
        super().__init__(strategy)
        self.doppole = "doppole"

    def outputinfo(self):
        return self.strategy.outputinfo(self.name, self.group, self.doppole)

    def inputargument(self, name_argument, argument):
        self.strategy.inputargument(self, name_argument, argument)

    def __str__(self):
        return "Имя: {} \t Группа: {} \t Допполе: {}".format(self.name, self.group, self.doppole)
