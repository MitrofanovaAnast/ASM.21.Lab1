from .user import user

class worker(user):
    def __init__(self, position='Worker'):
        user.__init__(self)
        self.salary=int()
        self.position=position

    def __str__(self):
        result=super().__str__()
        result+=f'Position: {self.position}' \
                f'Salary: {self.salary}\n'
        return result