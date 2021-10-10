import pickle


class FileOutputPickle:
    def do_input(self):
        with open('data.pickle', 'rb') as f:
            return pickle.load(f)

    def do_output(self, data):
        with open('data.pickle', 'wb') as f:
            pickle.dump(data, f)


class FileOutputShelve:
    def do_input(self):
        pass

    def do_output(self, data):
        pass

