
class user:
    def __init__(self):
        self.number=-1
        self.name=''
        self.age=int()

    def __str__(self):
        text = f'Number: {self.number}\n' \
               f'Name: {self.name}\n' \
               f'Age: {self.age}\n'
        return text

    def output(self, strategy):
        strategy(self).output()

    def input(self, strategy):
        strategy(self).input()