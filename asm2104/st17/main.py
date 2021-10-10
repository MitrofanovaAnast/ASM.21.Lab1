if __name__ == '__main__':
    from musList import musList
else:
    from .musList import musList

def closing():
    exit(0)

musList=musList()
container = {
    1: ("Добавить элемент", musList.add),
    2: ("Вывести элементы на экран", musList.print),
    3: ("Выгрузить в файл", musList.file_write),
    4: ("Загрузить из файла", musList.file_read),
    5: ("Очистить", musList.clear),
    6: ("Редактировать", musList.change),
    7: ("Сменить вывод", musList.swapMode),
    0: ("Выйти", closing)
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


