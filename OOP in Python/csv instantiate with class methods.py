import csv
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

    @classmethod
    def csv_instantiate(cls):
        with open('data.csv','r') as f:
            reader = csv.DictReader(f)
            data = list(reader)

            for lis in data:
                print(lis)
Item.csv_instantiate()