class Student:
    def __init__(self):
        self.name = input('Введите имя\n')
        self.surname = input('Введите фамилию\n')
        self.averageRating = input('Введите средний балл\n')

    def __str__(self):
        return '{0} {1}. Средний балл: {2}. '.format(self.surname, self.name, self.averageRating)
