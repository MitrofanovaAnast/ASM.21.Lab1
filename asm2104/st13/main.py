if __name__ == '__main__':
    from AnimeList import AnimeList
else:
    from .AnimeList import AnimeList

def closing():
    exit(0)

AnimeList=AnimeList()
container = {
    1: ("Добавить сериал", AnimeList.add),
    2: ("Отобразить на экране ", AnimeList.print),
    3: ("Сохранить в файл", AnimeList.file_write),
    4: ("Загрузить из файла", AnimeList.file_read),
    5: ("Редактировать", AnimeList.change),
    6: ("Очистить всё", AnimeList.clear),
    0: ("Выход", closing)
}

def main():
    while True:
        print("------------------------------")
        for i, item in container.items():
            print(i, ": ", item[0])
        print("------------------------------")
        container[int(input())][1]()
    
        
if __name__ == '__main__':
    main()


