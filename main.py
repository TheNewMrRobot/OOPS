class Item:
    def __init__(self):
        pass
    def calculateTotal(self,x,y):
        return x * y
    


item = Item()
item.name = "laptop"
item.price = "1,50,000"
item.quantity = 1

print(item.name)