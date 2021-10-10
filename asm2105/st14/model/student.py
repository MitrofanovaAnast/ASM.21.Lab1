from .listEntry import listEntry

class student(listEntry):
    def __init__(self, strategy):
        listEntry.__init__(self, strategy)
        self.Class=int()

    def __str__(self):
        text=super().__str__()
        text+=f'Класс: {self.Class}\n'
        return text