##########9a
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S4 = 0
    for i in range(1, n + 1):  
        S4 += i * i  
    print(f"Tổng S4 = 1^2 + 2^2 + 3^2 + ... + n^2 là: {S4}")

###########9b
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S5 = 0
    for i in range(n):  
        S5 += (2 * i + 1) ** 3  
    print(f"Tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3 là: {S5}")

#########9c
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S6 = 0
    for i in range(1, n + 1):  
        S6 += (2 * i) ** 4 
    print(f"Tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4 là: {S6}")


