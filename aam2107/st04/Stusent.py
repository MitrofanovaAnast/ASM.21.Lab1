if __name__ == '__main__':
    from ConsoleIO import WebIO, ConsoleIO
else
    from .ConsoleIO import WebIO, ConsoleIO


class Student:
    def __init__(self, name='', surname='', age='', io=ConsoleIO()):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__io = io

    '''@property
    def out(self):
        return self.__output'''

    '''@out.setter
    def out(self, output) -> None:
        self.__output = output'''

    def output(self):
        self.__io.do_output(self)

    def input(self):
        self.__io.do_input(self)

    def name_and_age(self):
        return f'Имя: { self.__name }, Возраст: { self.__age }'

    def __str__(self):
        return "Имя: {}, Фамилия: {}, Возраст: {}".format(
            self.__name, self.__surname, self.__age
        )
