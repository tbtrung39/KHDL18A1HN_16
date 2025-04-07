# Bài 6: Nhập vào n, in ra n số nguyên tố đầu tiên (không dùng def)

n = int(input("Nhập số nguyên dương n: "))

dem = 0  # đếm số lượng số nguyên tố đã in ra
so = 2   # bắt đầu từ số 2 vì đó là số nguyên tố đầu tiên

while dem < n:
    la_nguyen_to = True
    i = 2
    while i * i <= so:
        if so % i == 0:
            la_nguyen_to = False
            break
        i += 1

    if la_nguyen_to:
        print(so, end=' ')
        dem += 1

    so += 1
