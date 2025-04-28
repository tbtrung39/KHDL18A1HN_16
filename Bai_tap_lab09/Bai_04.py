from itertools import permutations
n = int(input("Nhập số n: "))
numbers = list(range(1, n+1))
perms = permutations(numbers)
print(f"Tất cả hoán vị của {numbers}:")
for perm in list(perms):
    print(perm)