class Item:
    # if want to give discount for all items so
    dis_rate = 0.7
    all = []
    def __init__(self,name: str, price: float,quantity=0):
        assert price >= 0, f"price should not be lesser than zero {self.price}" 
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
    def calculateTotal(self):
        return self.price * self.quantity
    def applyDiscount(self):
        # if we use Item then it will take the defiend one in class
        # if we specify self.dis_rate that will take the discount value from the object
        self.price = self.price * Item.dis_rate
    
    def __repr__(self) -> str:
        return f"Item({self.name},{self.price},{self.quantity})"
    
item = Item("phone",1000,2)
item2 = Item("phone",1000,2)
item3 = Item("phone",1000,2)
item4 = Item("phone",1000,2)
item5 = Item("phone",1000,2)

# problem is we can see the object location memory thats not readable so use __rep
print(Item.all)

item.applyDiscount()
print(item.calculateTotal())
# print(item.calculateTotal())
# item.dis_rate = 0.5