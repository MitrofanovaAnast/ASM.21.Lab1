class Player:
    def __init__(self):
        self.name = input('Введите имя\n')
        self.number = input('Введите номер на футболке\n')
        self.nationality = input('Введите гражданство\n')

    def __str__(self):
        return '{0}. Номер {1}. Гражданство: {2}. '.format(self.name, self.number, self.nationality)
