class Item:
    def __init__(self,name: str, price: float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculateTotal(self):
        return self.price * self.quantity
    
item = Item("phone",1000,2)
print(item.calculateTotal())