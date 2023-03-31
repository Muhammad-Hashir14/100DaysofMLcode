class Item:
    _all = []
    discount = 0.8
    def __init__(self, Item_name, Item_price, Item_type):
        self.Item_name = Item_name
        self.Item_price = Item_price
        self.Item_type = Item_type
        self._all.append(self)

    def apply_discount(self):
        self.Item_price = self.Item_price * self.discount

    def __repr__(self):
        return f"Item({self.Item_name}, {self.Item_price} ,,{self.Item_type})"

item1 = Item("Pizza",1000,"large")
item2 = Item("Burger",1100,"pizza burger")
item3 = Item("lasagnia",1200,"small")
item4 = Item("pasta",1400,"Normal")
item5 = Item("kabab",800,"5")

print(item1.Item_price)
item1.apply_discount()
print(item1.Item_price)

print(Item._all)

# to accessing all items seperatly
for name in Item._all:
    print(name.Item_name)

for price in Item._all:
    print(price.Item_price)

for type_ in Item._all:
    print(type_.Item_type)

print(Item._all)