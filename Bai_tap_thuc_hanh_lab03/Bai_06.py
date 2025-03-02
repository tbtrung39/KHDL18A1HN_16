n = int(input("Nhập số nguyên n: "))
tong = 0
for i in range(0,n+1):
    tong += i**3
print(f"Tổng bậc 3 của {n} là: {tong} ")