from .Starosta import Starosta
from .Student import Student
from .Strategy import ConcreteStrategyStudent, ConcreateStrategyStarosta, PickleStategy


class Spisok:

    def __init__(self):
        self.functions = {
            1: self.add,
            2: self.change,
            3: self.delete,
            4: self.output,
            5: self.write_file,
            6: self.read_file,
            7: self.clear,
            8: self.length,
            9: self.type
        }
        self.list_objects = []
        self.filestrategy = PickleStategy()

    # 1
    def add(self, switch, name, group, doppole=""):
        if switch == 1:
            var = Student(ConcreteStrategyStudent())
            var.inputargument("name", name)
            var.inputargument("group", group)
            self.list_objects.append(var)
        elif switch == 2:
            var2 = Starosta(ConcreateStrategyStarosta())
            var2.inputargument("name", name)
            var2.inputargument("group", group)
            var2.inputargument("doppole", doppole)
            self.list_objects.append(var2)

    # 2
    def change(self, switch, index, name, group, doppole=""):
        self.list_objects[index].inputargument("name", name)
        self.list_objects[index].inputargument("group", group)
        if switch == 2:
            self.list_objects[index].inputargument("doppole", doppole)

    # 3
    def delete(self, index):
        self.list_objects.pop(index)

    # 4
    def output(self):
        text: str = ""
        if len(self.list_objects) != 0:
            for i in range(len(self.list_objects)):
                text = "{} \n {} : {}".format(text, i, self.list_objects[i].outputinfo())
            return text
        else:
            return "List is empty"

    # 5
    def write_file(self):
        self.filestrategy.fileoutput(self.list_objects)
        return 'Writing is completed'

    # 6
    def read_file(self):
        self.list_objects = self.filestrategy.fileinput()
        return 'Reading is completed'

    # 7
    def clear(self):
        self.list_objects.clear()
        return "List is clear"

    # 8
    def length(self):
        return len(self.list_objects)

    #9
    def type(self, index):
        if type(self.list_objects[index]) == Student:
            return 1
        else:
            return 2
