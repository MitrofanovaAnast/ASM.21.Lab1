

class Member:

    def __init__(self):
        self.name = input('Enter name\n')
        self.surname = input('Enter surname\n')
        self.age = input('Enter age\n')
        self.id = ''

    def __str__(self):
        text = f'Name: {self.name}\n' \
               f'Surname: {self.surname}\n' \
               f'Age: {self.age}\n'
        return text
