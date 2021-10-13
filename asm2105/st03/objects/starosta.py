from .student import student

class starosta(student):

    def __init__(self, strategy):
        student.__init__(self, strategy)
        self.group_mail = ''

    def __str__(self):
        text=super().__str__()
        text+=f'Почта группа: {self.group_mail}\n'
        return text
