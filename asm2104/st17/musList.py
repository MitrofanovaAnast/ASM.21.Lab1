from single import single
from album import album
from strategies import Plain, Formatted, PickleDump, PickleLoad

class musList:
    def __init__(self):
        self.strategy=Plain()
        self.List=[]
        self.chosen='Plain'
        
    def assignStrategy(self):
        if self.chosen=='Formatted':
            self.strategy=Formatted()
        else:
            if self.chosen=='Plain':
                self.strategy=Plain()
        
    def add(self):
        case = int(input("0 - сингл, 1  - альбом: \n"))
        entity = album() if case else single()
        entity.input()
        self.List.append(entity)
        
    def print(self):
        self.strategy.print(self.List)
        
    def clear(self):
        self.List.clear()
        
    def file_write(self):
        self.strategy=PickleDump()
        self.strategy.print(self.List)
        self.assignStrategy()
    
    def file_read(self):
        self.strategy=PickleLoad()
        self.List=self.strategy.print(self.List)
        self.assignStrategy()
    
    def change(self):
        self.List[-1+int(input("Какой элемент вы бы хотели изменить?"))].input()
    
    def swapMode(self):
        if self.chosen=='Formatted':
            self.chosen='Plain'
            self.assignStrategy()
        else:
            self.chosen='Formatted'
            self.assignStrategy()
        
   