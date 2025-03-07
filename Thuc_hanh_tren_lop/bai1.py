################a
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số nhập vào phải lớn hơn 0. Vui lòng nhập lại n: "))
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print(f"Tổng S4 = 1^2 + 2^2 + ... + {n}^2 là: {S4}")


#############b
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số nhập vào phải lớn hơn 0. Vui lòng nhập lại n: "))
S5 = 0
i = 1
while i <= (2 * n + 1):
    S5 += i**3
    i += 2  
print(f"Tổng S5 = 1^3 + 3^3 + 5^3 + ... + (2n+1)^3 là: {S5}")


##########c
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số nhập vào phải lớn hơn 0. Vui lòng nhập lại n: "))
S6 = 0
i = 2  
while i <= 2 * n:
    S6 += i**4
    i += 2  
print(f"Tổng S6 = 2^4 + 4^4 + 6^4 + ... + (2n)^4 là: {S6}")
