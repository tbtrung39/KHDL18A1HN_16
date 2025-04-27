import random
n = int(input("Nhập số tự nhiên n: "))

A = [i for i in range(1, n + 1)]

result = []

while A:
    chon = random.choice(A)
    result.append(chon)
    A.remove(chon)  

print("Hoán vị ngẫu nhiên là:", result)
