from .student import student

class proforg(student):
    def __init__(self):
        student.__init__(self)
        self.profileTicketNumber = int()

    def __str__(self):
        result = super().__str__()
        result += f'Profile ticket number: {self.profileTicketNumber}'
        return result
