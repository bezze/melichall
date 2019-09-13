import json

from translate import Item


data_frave = open('frave-scrap/processed_products.json').read()
frave = json.loads(data_frave)

frave_items = []
for name, item in frave.items():
    frave_items.append(Item.from_frave(item))

first = frave_items[0]
for i in frave_items[1:]:
    print(first.similitude(i))
