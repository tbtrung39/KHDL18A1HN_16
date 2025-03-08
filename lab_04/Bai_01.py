#a
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số không hợp lệ! Nhập lại số nguyên dương n: "))
S4 = 0
i = 1
while i <= n:
    S4 += i**2
    i += 1
print("Tổng S4 =", S4)


#b
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số không hợp lệ! Nhập lại số nguyên dương n: "))
S5 = 0
i = 1
while i <= 2*n + 1:
    S5 += i**3
    i += 2
print("Tổng S5 =", S5)



#c
n = int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n = int(input("Số không hợp lệ! Nhập lại số nguyên dương n: "))
S6 = 0
i = 2
while i <= 2*n:
    S6 += i**4
    i += 2
print("Tổng S6 =", S6)


