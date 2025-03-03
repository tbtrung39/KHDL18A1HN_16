n = int(input("Nhap mot so: "))
tong = 0
for i in range(1, n + 1):
    tong += i**3
print(f"Tong bac 3 cua {n} so nguyen dau tien la {tong}.")