import pickle

class storagePickle:
    def store(self, obj):
        with open('elzadb.db', 'wb') as file:
            pickle.dump(obj, file)

    def load(self):
        with open('elzadb.db', 'rb') as file:
            return pickle.load(file)