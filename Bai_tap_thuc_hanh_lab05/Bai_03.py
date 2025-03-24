
n = int(input("Nhập số nguyên dương: "))
n2 = n
str = ""
while True:
    n1 = n % 2
    if n1 == 1:
        str = "1" + str
    elif n1 == 0:
        str = "0" + str
    n = n // 2
    if n == 0:
        break
print(f"{n2} chuyển sang hệ nhi phân là: {str}")