N = int(input("Nhập n: "))
tong = 0  
for i in range(1, N + 1):  
    tong += i**3  
print("Tổng bậc 3 của", N, "số nguyên đầu tiên là:", tong)