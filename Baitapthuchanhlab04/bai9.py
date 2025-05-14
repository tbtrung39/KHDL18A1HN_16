so = int(input("Nhập một số nguyên: "))

tong_chu_so = 0
while so > 0:
    chu_so = so % 10
    tong_chu_so += chu_so
    so //= 10

print("Tổng các chữ số là:", tong_chu_so)