from .item import item

class student(item):
    group=''
    def __init__(self, strategy):
        item.__init__(self, strategy)

    def __str__(self):
        text=super().__str__()
        text+=f'Группа: {self.group}\n'
        return text

