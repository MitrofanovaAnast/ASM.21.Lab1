from .worker import worker

class chef(worker):
    def __init__(self):
        worker.__init__(self, 'Chef')
        self.phone = ''

    def __str__(self):
        result = super().__str__()
        result += f'Phone: {self.phone}\n'
        return result