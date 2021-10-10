if __name__ == '__main__':
    from ConsoleIO import ConsoleIO
else:
    from .ConsoleIO import ConsoleIO


class Player():

    def __init__(self, name=' ', surname=' ', age=' '):
        self.surname = surname
        self.name = name
        self.age = age
        self.console = ConsoleIO()

    def write_data(self):
        self.name = self.console.Input("Имя: ", )
        self.surname = self.console.Input("Фамилия: ", )
        self.age = self.console.Input("Возраст: ", )

    def read_data(self):
        self.console.Output(self)

    def __str__(self):
        return "Имя: {} \nФамилия: {} \nВозраст: {}".format(
            self.name, self.surname, self.age
        )

