from collections import OrderedDict
ordereddict=OrderedDict()

n=int(input())
for i in range(n):
    item,space,price=input().rpartition(' ')
    if item not in ordereddict:
        ordereddict[item]=int(price)
    else:
        ordereddict[item]+=int(price)
for item_name,item_price in ordereddict.items():
    print(item_name,item_price)
