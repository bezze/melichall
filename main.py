import json
from translate import Item


data_frave = open('frave-scrap/processed_products.json').read()
frave = json.loads(data_frave)
frave_items = []
frave_ = []

data_garba = open('garba-scrap/processed_products.json').read()
garba = json.loads(data_garba)
garba_items = []
garba_ = []

for name, item in frave.items():
    frave_items.append(Item.from_frave(item))
    frave_.append(item)

for name, item in garba.items():
    garba_items.append(Item.from_garba(item))
    garba_.append(item)


sim_matrix = []

for fitem in frave_items:
    row = []
    for gitem in garba_items:
        s = fitem.similitude(gitem)
        row += [s]
        if fitem.model in gitem.name:
            print("model match")
            print(s)
            print(fitem)
            print(gitem)
    sim_matrix += [row]


header = 4*" " + (7*" ").join([f"{c:02d}  " for c in range(len(garba_items))])
print(header)
for i, row in enumerate(sim_matrix):
    str_row = "["+", ".join([f"{j:.2f} {k:.2f}" for j, k in row])+"]"
    print(f"{i:02d}", str_row)
