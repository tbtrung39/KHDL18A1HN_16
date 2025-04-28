import random

def permutation(a, result):
    if len(a) == 0:
        print(result)
        return
    idx = random.randint(0, len(a) - 1)
    result.append(a[idx])
    a.pop(idx)
    permutation(a, result)

n = int(input("Nhập số n: "))
a = list(range(1, n+1))
result = []

permutation(a, result)
