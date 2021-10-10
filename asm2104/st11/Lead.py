from asm2104.st11.Employee import Employee


class Lead(Employee):
    def __init__(self, lenght):
        Employee.__init__(self, lenght)
        self.position = 'lead'
        self.department = input('Input department: ')

    def __str__(self):
        text = super().__str__()
        text += 'Department: {0}'.format(self.department) + '\n\n'
        return text
