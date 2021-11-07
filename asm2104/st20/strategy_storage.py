
#Файл, содержащий код стратегии

import pickle
from typing import List


class Storage:
    def input(self):
        pass

    def output(self, data: List):
        pass


class FileInputOutPut(Storage):
    def input(self):
        with open('groups.pickle', 'rb') as f:
            return pickle.load(f)

    def output(self, members: List):
        with open('groups.pickle', 'wb') as f:
            pickle.dump(members, f)
