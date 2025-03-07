n = int(input("Nhập số n bất kì: "))
x = n
s = 0
while True:
    n1 = x % 10
    s += n1
    x = x // 10
    if x == 0:
        break
print(f"tổng sô {n} là: {s}")