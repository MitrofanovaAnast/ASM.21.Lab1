from .Strategy import Strategy


class Student:

    def __init__(self, strategy: Strategy):
        self.strategy = strategy
        self.name = "name"
        self.group = "group"

    def outputinfo(self):
        self.strategy.outputinfo(self)

    def inputargument(self):
        self.strategy.inputargument(self)

    def __str__(self):
        return "Имя: {} \t Группа: {}".format(self.name, self.group)
