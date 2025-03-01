n = int(input("Nhap n: "))
tong = 0

for i in range(1, n + 1):
    tu_so = 2 * i + 1
    mau_so = 2 * i + 3
    tong += (tu_so / mau_so)

print("Ket qua cua bieu thuc:", round(tong, 3))
