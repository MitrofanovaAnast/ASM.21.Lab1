
class zapis:
    def __init__(self):
        self.id = -1
        self.name = ''
        self.age = int()
        self.gender = ''

    def __str__(self):
        text = f'Number: {self.id}\n' \
               f'Name: {self.name}\n' \
               f'Age: {self.age}\n' \
               f'Gender: {self.gender}\n'
        return text

    def output(self, strategy):
        strategy(self).output()

    def input(self, strategy):
        strategy(self).input()

