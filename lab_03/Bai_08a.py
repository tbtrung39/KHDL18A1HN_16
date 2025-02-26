
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương lớn hơn 0.")
else:
    S1 = 0
    for i in range(1, n + 1):
        S1 += i
    print("Tổng S1 =",S1)