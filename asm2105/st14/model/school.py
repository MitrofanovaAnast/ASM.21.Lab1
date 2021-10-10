
class school:
    def __init__(self, storage):
        self.list={}
        self.storage=storage()

        try:
            self.load()
        except:
            pass

    def save(self):
        self.storage.save(self.list)

    def load(self):
        self.list=self.storage.load()
        # print(self.list)

    def add(self, item):
        item.id=len(self.list)
        self.list[item.id]=item
        return item.id

    def clear(self):
        self.list.clear()

    def search(self, param):
        try:
            if int(param) in self.list:
                return self.list[int(param)]
        except:
            for item in self.list.values():
                if item.name==param:
                    return item
