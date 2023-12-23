from functools import cmp_to_key
val = [120,100,60]
wts = [30,20,10]
cap = 50

class Items:
    def __init__(self, val, wt, ppu):
        self.val = val
        self.wt = wt
        self.ppu = ppu # price per unit

# comparator to compare ppu value of Item objects
def compare(v1, v2):
    if v1.ppu < v2.ppu:
        return -1
    elif v1.ppu > v2.ppu:
        return 1
    else:
        return 0

n = len(val)
items = [] # create an array to store Item objects
for i in range(n):
    ppu = val[i]/wts[i]
    temp = Items(val[i], wts[i], ppu)
    items.append(temp)

items = sorted(items, key=cmp_to_key(compare)) # sort the array

ans = 0
for i in range(n-1,-1,-1): # start from object having highest ppu
    if items[i].wt > cap:
        ans += items[i].ppu * cap
        cap = 0
    else:
        ans += items[i].val
        cap -= items[i].wt

print(ans) 
