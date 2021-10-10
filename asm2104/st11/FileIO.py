import pickle


class FileIO:
    @staticmethod
    def output(e_list):
        with open('asm2104/st11/output.pickle', 'wb') as f:
            pickle.dump(e_list, f)

    @staticmethod
    def input(lenght, e_list):
        with open('asm2104/st11/output.pickle', 'rb') as f:
            return pickle.load(f)
