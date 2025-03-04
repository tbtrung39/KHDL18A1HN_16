n = int(input("Nhập số n: "))
tong = 0  

for i in range(1, n + 1):  
    tong += (2 * i) / (3 * i + 1)  

print(f"Tổng = {tong:.3f}")  