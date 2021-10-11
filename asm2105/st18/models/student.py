
from .item import item

class student(item):
    def __init__(self, interactive):
        item.__init__(self, interactive)
        self.course=int()
        self.group=''

    def __str__(self):
        text=super().__str__()
        text+=f'Курс: {self.course}\n' \
              f'Группа: {self.group}\n'
        return text
