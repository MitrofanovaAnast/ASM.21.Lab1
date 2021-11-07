class IO:
    def enter(self, person):
        pass

    def output(self, data):
        pass


class ConsoleInputOutPut(IO):
    def enter(self, person):
        print(person.__dict__.items())
        for key, val in person.__dict__.items():
            person.__dict__[key] = input(f"{ key }: ")

    def output(self, data):
        print('-------Вывод пользователей----------')
        for person in data:
            for key, val in person.__dict__.items():
                print(f"{key} : {val}")
            print("\n")
        print('---------------------------------')
