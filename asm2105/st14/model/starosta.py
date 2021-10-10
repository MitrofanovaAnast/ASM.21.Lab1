from .student import student

class starosta(student):
    def __init__(self, strategy):
        student.__init__(self, strategy)
        self.email=''

    def __str__(self):
        text=super().__str__()
        text+=f'Почта группы: {self.email}\n'
        return text