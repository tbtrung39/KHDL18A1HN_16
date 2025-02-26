n = int(input("Nhập n: "))
tong = 0
for i in range(1, n + 1):
    tong += (2 * i + 1) / (2 * i + 3)
print("Kết quả là %0.3f"%tong)
