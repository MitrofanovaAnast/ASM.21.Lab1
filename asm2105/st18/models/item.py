

class item:
    def __init__(self, interactive):
        self.id=-1
        self.name=''
        self.age=int()
        self.interactive=interactive()

    def __str__(self):
        text=f'Номер: {self.id}\n' \
             f'Имя: {self.name}\n' \
             f'Возраст: {self.age}\n'
        return text

    def Print(self):
        self.interactive.Print(self)

    def Enter(self):
        self.interactive.Enter(self)