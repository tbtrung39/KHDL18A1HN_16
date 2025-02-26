
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương lớn hơn 0.")
else:
    S4 = 0
    for i in range(1, n + 1):
        S4 += i**2
    print("Tổng S4 =", S4)