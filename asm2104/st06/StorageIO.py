import pickle
import shelve


class Pickle:
    @staticmethod
    def dump(list):
        with open('asm2104/st06/pickle_storage.pickle', 'wb') as f:
            pickle.dump(list, f)

    @staticmethod
    def load(list):
        with open('asm2104/st06/pickle_storage.pickle', 'rb') as f:
            return pickle.load(f)


class Shelve:
    @staticmethod
    def dump(list):
        with shelve.open('asm2104/st06/shelve_storage') as f:
            f['key'] = list
            f.close()

    @staticmethod
    def load(listw):
        with shelve.open('asm2104/st06/shelve_storage') as f:
            return list(f['key'])
