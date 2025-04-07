import random

ds = [0,1,2,3,4,5,6,7,8,9]
chon = random.sample(ds, 5)

A = set()
for x in chon:
    A.add(x)

print("Tập hợp A:", A)
