from .worker import worker

class teacher(worker):
    def __init__(self, strategy):
        worker.__init__(self, strategy)
        self.subject=''

    def __str__(self):
        text=super().__str__()
        text+=f'Предмет: {self.subject}\n'
        return text