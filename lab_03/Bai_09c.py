
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương lớn hơn 0.")
else:
    S6 = 0
    for i in range(2, 2*n + 1, 2): 
        S6 += i**4
    print("Tổng S6 =",S6)