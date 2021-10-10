
from Adaptation import Adaptation
from Original import Original
from Function import Simple, Editing, PickleDump, PickleLoad

class AnimeList:
    def __init__(self):
        self.strategy=Simple()
        self.List=[]
        self.chosen='Simple'
        
    def assignStrategy(self):
        if self.chosen=='Editing':
            self.strategy=Editing()
        else:
            if self.chosen=='Simple':
                self.strategy=Simple()
        
    def add(self):
        case = int(input("Выберите: \n 0 - Адаптация, 1  - Оригинал: \n------------------------------------ \n *Адаптация - сериал, основанный на манге, новелле или серии романов \n *Оригинал - сериал, с собственным, новым сюжетом \n " ))
        entity = Original() if case else Adaptation()
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
        self.List[-1+int(input("Какой сериал вы бы хотели изменить? (Введите порядковый номер)"))].input()

        
   