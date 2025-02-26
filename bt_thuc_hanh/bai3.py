import math
n = int(input("Nhập n: "))
a = True
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        a = False
        break
if a and n > 1:
    print(f"{n} là số nguyên tố")
else:
    found = False
    duoi = n - 1
    tren = n + 1
    while not found:
        for i in range(2, int(math.sqrt(duoi)) + 1):
            if duoi % i == 0:
                break
        else:
            print(f"Số nguyên tố gần nhất: {duoi}")
            break
        for i in range(2, int(math.sqrt(tren)) + 1):
            if tren % i == 0:
                break
        else:
            print(f"Số nguyên tố gần nhất: {tren}")
            break
        duoi -= 1
        tren += 1
