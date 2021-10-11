from .student import student

class proforg(student):
    def __init__(self, interactive):
        student.__init__(self, interactive)
        self.phone=''

    def __str__(self):
        text=super().__str__()
        text+=f'Телефон: {self.phone}\n'
        return text