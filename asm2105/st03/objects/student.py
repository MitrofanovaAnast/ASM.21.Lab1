from .item import item

class student(item):

    def __init__(self, strategy):
        item.__init__(self, strategy)
        self.group=''

    def __str__(self):
        text=super().__str__()
        text+=f'Группа: {self.group}\n'
        return text


