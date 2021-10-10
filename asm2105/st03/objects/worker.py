from .item import item

class worker(item):
    experience=int()
    def __init__(self, strategy):
        item.__init__(self, strategy)

    def __str__(self):
        text=super().__str__()
        text+=f'Стаж: {self.experience}\n'



