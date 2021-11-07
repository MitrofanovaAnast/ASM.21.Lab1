class Developer:
    def __init__(self):
        self.name = input('Введите имя\n')
        self.programLanguage = input('Введите язык программирования\n')
        self.salary = input('Введите оклад\n')

    def __str__(self):
        return '{0}.\nЯзык программирования - {1}.\nОклад: {2}.\n'.format(self.name, self.programLanguage, self.salary)
