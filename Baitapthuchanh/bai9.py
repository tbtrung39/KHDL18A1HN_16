n = int(input("Nhập số nguyên dương n: "))  
if n <= 0:
    n = int(input("n phải là số nguyên dương. Nhập lại: "))
S4 = 0  
S5 = 0  
S6 = 0  
# Tính tổng S4
for i in range(1, n + 1):  
    S4 += i ** 2  # S4 = 1^2 + 2^2 + ... + n^2  
# Tính tổng S5
for i in range(1, n + 1):  
    S5 += (2 * i - 1) ** 3  # S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3  
# Tính tổng S6
for i in range(1, n + 1):  
    S6 += (2 * i) ** 4  # S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4  
# In kết quả
print("S4 =", S4)  
print("S5 =", S5)  
print("S6 =", S6)