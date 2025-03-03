
n = int(input("Nhập số nguyên dương n: "))
if n <= 0:
    print("Vui lòng nhập số nguyên dương lớn hơn 0.")
else:
    tong_nghich_dao = 0
    for i in range(1, n + 1):
        tong_nghich_dao += 1 / i
    print("Tổng nghịch đảo của", n, "số nguyên đầu tiên là:", tong_nghich_dao)