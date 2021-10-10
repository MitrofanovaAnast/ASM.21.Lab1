from .group import Group
from .consoleIO import ConsoleIO

def main():
	group = Group()
	menu = {
	1:('Добавить объект определенного типа',group.addNewPerson),
	2:('Удалить объект',group.deleteOneElement),
	3:('Вывести список',group.dumpAllObjects),
	4:('Сохранить в файл',group.dumpData),
	5:('Загрузить из файла',group.loadData),
	6:('Очистить список',group.clearList),
}
	while True:
		for i, item in menu.items():
			print('{0}. {1}'.format(i, item[0]))
		menu[int(input())][1]()


if __name__ == '__main__':
	main()