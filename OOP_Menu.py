class MenuItem:
    def __init__ (self):
        self.name=""
        self.price=0
    def Show(self):#def Show (class method)
        print("%s        %i"%(self.name, self.price))
        
Spag=MenuItem()#data type: Menu Item (instance)
Spag.name="Spaghetti"
Spag.price=95#price (class member)

Coke=MenuItem()
Coke.name="Coke Float"
Coke.price=25

Spag.Show()
Coke.Show()

