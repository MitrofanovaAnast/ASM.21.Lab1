from .student import student

class starosta(student):
    def __init__(self, type='student'):
        student.__init__(self, type)
        self.groupEmail=''

    def __str__(self):
        result=super().__str__()
        result+=f'Group e-mail: {self.groupEmail}\n'
        return result