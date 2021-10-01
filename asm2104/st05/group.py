import sys
from person import Student, MainStudent
from inp_out import StrategyIO
from storage import Storage


class Group:
	members = []

	def __init__(self, strategy_io: StrategyIO, strategy_storage: Storage):
		self._strategy_io = strategy_io
		self._strategy_storage = strategy_storage

	@property
	def strategy_io(self) -> StrategyIO:
		"""
		Cообщит класс стратегии ввода вывода
		:return:
		"""
		return self._strategy_io

	@property
	def strategy_storage(self) -> Storage:
		"""
		Cообщит класс стратегии хранения
		:return:
		"""
		return self._strategy_storage

	@strategy_io.setter
	def strategy_io(self, strategy: StrategyIO) -> None:
		"""
		Поменять стратегию ввода/вывода в интерактивном режиме
		:param strategy:
		:return:
		"""
		self._strategy_io = strategy

	@strategy_storage.setter
	def strategy_storage(self, strategy: Storage) -> None:
		"""
		Поменять стратегию хранения в интерактивном режиме
		:param strategy:
		:return:
		"""
		self._strategy_storage = strategy

	def add_member(self):
		"""
		Добавит участника
		:return:
		"""
		case = int(input("0 - Студент, 1  - Староста: \n"))
		person = MainStudent() if case else Student()
		self.member_from_console(person)
		self.members.append(person)

	def member_from_console(self, person):
		"""
		Заполнить участника в консоли
		:param person:
		:return:
		"""
		self._strategy_io.enter(person)

	def members_in_console(self):
		"""
		Выведет всех участников в консоль
		:return:
		"""
		self._strategy_io.output(self.members)

	def members_from_file(self):
		"""
		Загрузит участников с файла
		:return:
		"""
		self.members = self._strategy_storage.input()

	def members_in_file(self):
		"""
		Запишет участников в файл
		:return:
		"""
		self._strategy_storage.output(self.members)

	def delete_members(self):
		"""
		Почистить список участников
		:return:
		"""
		del self.members[:]

	def edit_members(self):
		"""
		Изменить конкретного участника
		:return:
		"""
		print('Введите id участника в базе.')
		try:
			case = int(input("Целое положительное число: "))
		except ValueError:
			print("Введите целое положительное число!")
			sys.exit()
		try:
			person = self.members[case]
		except IndexError:
			print(f"Участника с таким id :{case} нет в базе!")
			sys.exit()
		self.member_from_console(person)
