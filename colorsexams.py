class Colors:
    def __init__(self, color):
        self.color=color
    def show(self):
        print("%s"%(self.color))

ListOfColors=[]
info=Colors("Red")
ListOfColors.append(info)
info=Colors("Green")
ListOfColors.append(info)
info=Colors("Blue")
ListOfColors.append(info)
class Pink(Colors):
    pass
class Yellow(Colors):
    pass

for info in ListOfColors:
    info.show()
