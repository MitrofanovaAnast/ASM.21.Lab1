from asm2105.st10.player import Player
from asm2105.st10.captain import Captain


menu = [
    {'label': 'Добавить обычного футболиста', 'class': Player},
    {'label': 'Добавить капитана', 'class': Captain}
]


class ConsoleIO:
    @staticmethod
    def dump(array):
        for item in array:
            print(item)

    @staticmethod
    def load():
        result = []
        counter = int(input('Сколько футболистов добавляем?\n'))
        for i in range(counter):
            for j in range(len(menu)):
                print('{0} - {1}'.format(j, menu[j]['label']))

            result.append(menu[int(input())]['class']())
        return result
