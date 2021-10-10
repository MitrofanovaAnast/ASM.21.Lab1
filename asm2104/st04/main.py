from group import Group
from consoleIO import ConsoleIO

def main():
	group = Group()
	menuDict = {
	1:('Добавить элемент',group.addElement),
	2:('Очистить список',group.clearList),
	3:('Вывод списка на экран',group.outputConsole),
	4:('Запись в файл',group.outputFile),
	5:('Чтение из файла',group.inputFile),
	6:('Удалить объект',group.deleteObject),
	7:('Редактировать',group.editObject)
}
	while True:
		for i, item in menuDict.items():
			print(str(i)+'. '+ item[0])
		menuDict[int(input())][1]()


if __name__ == '__main__':
	main()