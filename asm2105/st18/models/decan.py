from .employe import employe

class decan(employe):
    def __init__(self, interactive):
        employe.__init__(self, interactive)
        self.faculty=''

    def __str__(self):
        text=super().__str__()
        text+=f'Факультет: {self.faculty}\n'
        return text
