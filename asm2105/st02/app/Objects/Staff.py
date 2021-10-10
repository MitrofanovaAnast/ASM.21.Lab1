from .Item import Item

class Staff(Item):
    post=''
    experience=''
    def __init__(self, strategy):
        Item.__init__(self, strategy)

    def __str__(self):
        text = super().__str__()
        text += 'Занимаемая должность: {} \n Стаж работы: {} \n'.format(self.post, self.experience)
        return text

    def get_attribs(self):
        attribs = super().get_attribs()
        attribs['post'] = 'Занимаемая должность'
        attribs['experience'] = 'Cтаж работы'
        return attribs