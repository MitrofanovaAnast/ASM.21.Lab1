class Salesman:
    def __init__(self, name, salary, stake):
        self.name = name
        self.salary = salary
        self.stake = stake

    @staticmethod
    def newSalesman(count):
        name = input(f'{count} - Введите ФИО\n')
        salary = input(f'{count} - Введите зарплату\n')
        stake = input(f'{count} - Введите ставку\n')
        return Salesman(name, salary, stake)

    def __str__(self):
        return 'ФИО: {}, З/П: {}, Ставка: {}, '.format(self.name, self.salary, self.stake)
