# Bài 2: Tìm số hoàn hảo nhỏ hơn n
n = int(input("Nhập n: "))
x = 1
while x < n:
    tổng_uoc = 0
    y = 1
    while y < x:
        if x % y == 0:
            tổng_uoc = tổng_uoc + y
        y = y + 1
    if tổng_uoc == x:
        print("Số hoàn hảo:", x)
    x = x + 1