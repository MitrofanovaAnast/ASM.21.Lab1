from .Starosta import Starosta
from .Student import Student
from .Strategy import PickleStategy, ConsoleIO


class Spisok:
    def __init__(self):
        self.functions = {
            1: self.add,
            2: self.change,
            3: self.delete,
            4: self.output,
            5: self.write_file,
            6: self.read_file,
            7: self.clear
        }
        self.list_objects = []
        self.filestrategy = PickleStategy()
    # 1
    def add(self):

        switch = int(input(r"""
        1 - Student
        2 - Starosta
        Input = """))

        if switch == 1:
            var = Student(ConsoleIO())
        elif switch == 2:
            var = Starosta(ConsoleIO())
        else:
            print('incorrect input')
        var.inputargument()
        self.list_objects.append(var)

    # 2
    def change(self):
        if len(self.list_objects) != 0:
            #self.output()
            index = int(input("\n index = "))
            self.list_objects[index].inputargument()
        else:
            print('List is empty')

    # 3
    def delete(self):
        if len(self.list_objects) != 0:
            #self.output()
            index = int(input("\n index = "))
            self.list_objects.pop(index)
        else:
            print('List is empty')


    # 4
    def output(self):
        if len(self.list_objects) != 0:
            for i,o in enumerate(self.list_objects):
                print(i)
                o.outputinfo()
        else:
            print("List is empty")

    # 5
    def write_file(self):
        self.filestrategy.fileoutput(self.list_objects)

    # 6
    def read_file(self):
        self.list_objects = self.filestrategy.fileinput()

    # 7
    def clear(self):
        self.list_objects.clear()

