from .ConsoleIO import ConsoleIO


class Employee:
    def __init__(self, name='', surname='', age='', salary='', io=ConsoleIO()):
        self.name = name
        self.surname = surname
        self.age = age
        self.salary = salary
        self.io = io

    def output(self):
        self.io.do_output(self)

    def input(self):
        self.io.do_input(self)

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}, Зарплата: {}".format(
            self.name, self.surname, self.age, self.salary
        )