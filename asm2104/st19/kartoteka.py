
class kartoteka:
    def __init__(self):
        self.container=dict()

    def store(self, strategy):
        strategy().store(self)

    def load(self, strategy):
        self.__dict__.update(strategy().load().__dict__)

    def add_member(self, element):
        element.number=len(self.container)
        self.container[element.number]=element
        return element.number

    def get_member(self, item):
        if int(item) in self.container:
            return self.container[int(item)]
        else:
            result=[]
            for user in self.container.values():
                if item==user.name:
                    result.append(user)
            return result


    def clr(self):
        self.container.clear()