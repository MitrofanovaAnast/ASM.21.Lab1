from asm2104.st15.salesman import Salesman


class Administrator(Salesman):
    def __init__(self, name, salary, stake, level):
        super(Administrator, self).__init__(name, salary, stake)
        self.level = level

    def __str__(self):
        return super(Administrator, self).__str__() + f'Уровень: {self.level}'

    @staticmethod
    def newSalesman(count):
        name = input(f'{count} - Введите ФИО\n')
        salary = input(f'{count} - Введите зарплату\n')
        stake = input(f'{count} - Введите ставку\n')
        level = input(f'{count} - Введите уровень\n')
        return Administrator(name, salary, stake, level)
