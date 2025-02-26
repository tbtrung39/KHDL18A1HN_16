
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương lớn hơn 0.")
else:
    S5 = 0
    for i in range(1, 2*n + 2, 2):  
        S5 += i**3
    print("Tổng S5 =", S5)