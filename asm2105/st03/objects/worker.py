from .item import item

class worker(item):

    def __init__(self, strategy):
        item.__init__(self, strategy)
        self.experience=int()

    def __str__(self):
        text=super().__str__()
        text+=f'Стаж: {self.experience}\n'
        return text



