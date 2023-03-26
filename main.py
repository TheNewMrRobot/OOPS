class Item:
    # if want to give discount for all items so
    dis_rate = 0.7
    all = []
    def __init__(self,name: str, price: float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
    def calculateTotal(self):
        return self.price * self.quantity
    def applyDiscount(self):
        # if we use Item then it will take the defiend one in class
        # if we specify self.dis_rate that will take the discount value from the object
        return self.price * Item.dis_rate
    
item = Item("phone",1000,2)
item2 = Item("phone",1000,2)
item3 = Item("phone",1000,2)
item4 = Item("phone",1000,2)
item5 = Item("phone",1000,2)

print(Item.all)
# print(item.calculateTotal())
# item.dis_rate = 0.5