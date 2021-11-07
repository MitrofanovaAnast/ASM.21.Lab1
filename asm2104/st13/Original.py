if __name__ == '__main__':
    from Adaptation import Adaptation
else: 
    from .Adaptation import Adaptation
    
class Original(Adaptation):
    def __init__(self, name='', episodenum=24, genre=''):
        self.name=name
        self.genre=genre
        self.episodenum=episodenum

        
    def strSimple(self):
        return "Сериал:\n"+"Название:{} Жанр:{} Количество серий:{} ".format(self.name,self.genre,self.episodenum,)
        
    def strEditing(self):
        return "Сериал:\n"+"Название:{} Жанр:{} Количество серий:{} ".format(self.name,self.genre,self.episodenum,)
        
    def input(self):
        self.name=input("Название:")
        self.genre=input("Жанр:")
        self.episodenum=int(input("Количество серий:"))
