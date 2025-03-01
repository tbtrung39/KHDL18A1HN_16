############8a
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S1 = 0
    for i in range(1, n + 1):  
        S1 += i  
    print(f"Tổng S1 = 1 + 2 + 3 + ... + {n} là: {S1}")


###########8b
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S2 = 0
    for i in range(0, n):
        S2 += 2 * i + 1  
    print("Tổng S2 = 1 + 3 + 5 + ... + (2n+1) là:", S2)

##############8c
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập n là số nguyên dương (n > 0).")
else:
    S3 = 0
    for i in range(1, n + 1):
        S3 += 2 * i  
    print("Tổng S3 = 2 + 4 + 6 + ... + 2n là:", S3)


