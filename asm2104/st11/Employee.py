class Employee:

    def __init__(self, lenght):
        Employee.id = lenght + 1
        self.id = Employee.id
        self.full_name = input('Input full name: ')
        self.position = ''
        self.salary = input('Input salary: ')

    def __str__(self):
        text = 'ID: {0}'.format(self.id) + '\n' \
               'Full name: {0}'.format(self.full_name) + '\n' \
               'Position: {0}'.format(self.position) + '\n' \
               'Salary: {0}'.format(self.salary) + '\n'
        return text
