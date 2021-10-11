from .item import item

class employe(item):
    def __init__(self, interactive):
        item.__init__(self, interactive)
        self.roomNumber=int()

    def __str__(self):
        text=super().__str__()
        text+=f'Кабинет: {self.roomNumber}\n'
        return text