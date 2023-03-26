class Item:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculateTotal(self,x,y):
        return x * y
    
item = Item("phone",100000,2)
