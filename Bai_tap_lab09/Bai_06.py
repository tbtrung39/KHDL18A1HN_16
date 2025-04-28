import random
n = int(input("Nhập số n: "))
A = list(range(1, n+1))
result = []
while A:
    index = random.randint(0, len(A)-1)
    result.append(A.pop(index))
print("Hoán vị ngẫu nhiên:", result)