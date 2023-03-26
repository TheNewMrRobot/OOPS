class Item:
    def __init__(self,name: str, price: float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculateTotal(self,x,y):
        return x * y
    
item = Item("phone","1asdd",2)
print(item.price)