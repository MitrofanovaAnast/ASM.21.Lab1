from .worker import worker

class chef(worker):
    def __init__(self, type='worker'):
        worker.__init__(self, 'Chef', type)
        self.phone = ''

    def __str__(self):
        result = super().__str__()
        result += f'Phone: {self.phone}\n'
        return result