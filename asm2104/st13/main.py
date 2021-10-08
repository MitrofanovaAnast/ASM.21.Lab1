from asm2104.st13.ConsoleIO import ConsoleIO
from .group import Group

group = Group(ConsoleIO)
menu = [
	{'text': 'Добавить элемент', 'method': group.addElement},
	{'text': 'Очистить список', 'method': group.clearList},
	{'text': 'Отправить', 'method': group.dump},
	{'text': 'Получить', 'method': group.load},
]
def main():
	while True:
		for i in range(len(menu)):
			print('{0}. {1}'.format(i, menu[i]['text']))
		selected = int(input())
		menu[selected]['method']()



if __name__ == '__main__':
	main()


