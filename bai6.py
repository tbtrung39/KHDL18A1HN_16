import random

def permutation_m(a, result):
    if len(a) == 0:
        print(result)
        return
    idx = random.randint(0, len(a) - 1)
    result.append(a[idx])
    a.pop(idx)
    permutation_m(a, result)

n = int(input("Nhập n: "))
m = int(input("Nhập m: "))
a = []
for i in range(1, m+1):
    a.append(i)

result = []
permutation_m(a, result)
