from asm2104.st14.student import Student


class Headman(Student):
    def __init__(self):
        super(Headman, self).__init__()
        self.additionalScholarship = input('Введите дополнительную стипендию\n')

    def __str__(self):
        return super(Headman, self).__str__() + 'Дополнительная стипендия: {}'.format(self.additionalScholarship)
