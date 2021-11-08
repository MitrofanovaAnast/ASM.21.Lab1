import pickle

from .fileIO import FileIO
from .consoleIO import ConsoleIO
from .student import Student 
from .head import Head 

class Group:
    def __init__(self):
        self.list = []
        self.strategy=ConsoleIO()

    def addElement(self):
        self.changeStrategy(ConsoleIO())
        self.inputList()
        

    def clearList(self):
        self.list.clear()

    def deleteObject(self):
        if(len(self.list)==0):
            print('Список пуст')
        else:
            print('Введите индекс объекта, который нужно удалить')
            n=int(input())
            if(len(self.list)<=n):
                print('В списке нет элемента')
            else:
                self.list.pop(n)
    
    def editObject(self):
        if(len(self.list)==0):
            print('Список пуст')
        else:
            print('Введите индекс объекта, который нужно изменить')
            n=int(input())
            if(len(self.list)<=n):
                print('В списке нет элемента')
            else:
                self.list[n].inputProperties()

    def outputList(self):
        self.strategy.output(self.list)

    def inputList(self):
        return self.strategy.input(self.list)

    def outputConsole(self):
        self.strategy=ConsoleIO
        if(len(self.list)==0):
            print('Список пуст')
        else:
            self.changeStrategy(ConsoleIO())
            self.outputList()

    def changeStrategy(self,newStrategy):
        self.strategy=newStrategy


    def outputFile(self):
        self.changeStrategy(FileIO())
        self.outputList()

    def inputFile(self):
        self.changeStrategy(FileIO())
        self.list=self.inputList()