from asm2104.st11.Employee import Employee


class Developer(Employee):
    def __init__(self, lenght):
        Employee.__init__(self, lenght)
        self.position = 'developer'
        self.qualification = input('Input qualification: ')

    def __str__(self):
        text = super().__str__()
        text += 'Qualification: {0}'.format(self.qualification) + '\n\n'
        return text
