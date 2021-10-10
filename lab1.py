import asm2104.st00.main
import asm2105.st00.main
import aam2107.st00.main
#import aam2107.st14.main
import aam2107.st03.main
import asm2105.st04.main
import asm2104.st13.main
import asm2104.st04.main
import asm2105.st20.main
import aam2107.st04.main
import asm2105.st15.main
import asm2105.st02.main
#	добавить импорт своего модуля по шаблону
#	import asm<код группы>.st<номер по журналу>.main

MENU = [
		["[2104-00] Образец 2104", asm2104.st00.main.main],
		["[2105-00] Образец 2105", asm2105.st00.main.main],
		["[2107-00] Образец 2107", aam2107.st00.main.main],
#		добавить пункт меню для вызова своей главной функции по шаблону:
#		["[<код группы>-<номер по журналу>] <Фамилия>", <ссылка на функцию>],
		#["[2107-00] Sudakov", aam2107.st14.main.main],
		["[2107-00] Gladkov", aam2107.st03.main.main],
		["[2105-04] Dautov", asm2105.st04.main.main],
		["[2104-13] Pezhemsky", asm2104.st13.main.main],
		["[2104-04] Devin", asm2104.st04.main.main],
		["[2105-20 Kharisov", asm2105.st20.main.main],
		["[2107-04] Zhilina", aam2107.st04.main.main],
		["[2105-15] Semitko", asm2105.st15.main.main],
		["[2105-02] Astafeva", asm2105.st02.main.main]
]

def menu():
	print("------------------------------")
	for i, item in enumerate(sorted(MENU)):
		print("{0:2}. {1}".format(i, item[0]))
	print("------------------------------")
	return int(input())

try:
	while True:
		sorted(MENU)[menu()][1]()
except Exception as ex:
	print(ex, "\nbye")
