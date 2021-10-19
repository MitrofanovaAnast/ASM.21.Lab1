from .student import student

class starosta(student):
    def __init__(self):
        student.__init__(self)
        self.groupEmail=''

    def __str__(self):
        result=super().__str__()
        result+=f'Group e-mail: {self.groupEmail}\n'
        return result