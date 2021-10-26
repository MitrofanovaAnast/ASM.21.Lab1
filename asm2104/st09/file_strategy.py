import pickle


class FileStrategy:
    @staticmethod
    def dump(array):
        with open('save.pickle', 'wb') as f:
            pickle.dump(array, f)

    @staticmethod
    def load():
        with open('save.pickle', 'rb') as f:
            return pickle.load(f)
