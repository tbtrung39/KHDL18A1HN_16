
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập lại số nguyên dương lớn hơn 0.")
else:
    S3 = 0
    for i in range(2, 2*n + 1, 2):
        S3 += i
    print("Tổng S3 =", S3)