from .listEntry import listEntry

class worker(listEntry):
    def __init__(self, strategy):
        listEntry.__init__(self, strategy)
        self.salary=int()

    def __str__(self):
        text=super().__str__()
        text+=f'Зарплата: {self.salary}\n'
        return text
