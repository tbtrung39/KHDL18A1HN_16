# Bài 1: Tính tổng dãy số với 3 chữ số thập phân
n = int(input("Nhập n: "))
tổng = 1
i = 1
while i <= n:
    tử = 2 * i
    mẫu = (2 * i + 1)
    tổng = tổng + (tử / mẫu)
    i = i + 1

tổng = int(tổng * 1000) / 1000

print("Kết quả bài 1:", tổng)
