from aam2107.st11.pharman import Pharman


class Admin(Pharman):
    def __init__(self, name, salary, stake, level):
        super(Admin, self).__init__(name, salary, stake)
        self.level = level

    def __str__(self):
        return super(Admin, self).__str__() + f'Уровень: {self.level}'

    @staticmethod
    def newPharman(count):
        name = input(f'{count} - Введите ФИО\n')
        salary = input(f'{count} - Введите зп\n')
        stake = input(f'{count} - Введите ставку\n')
        level = input(f'{count} - Введите должность\n')
        return Admini(name, salary, stake, level)
