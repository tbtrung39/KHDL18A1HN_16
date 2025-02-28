# Bài 7: Tính tổng nghịch đảo của n số nguyên đầu tiên
n = int(input("Nhập n: "))
tổng = 0
i = 1
while i <= n:
    tổng = tổng + (1 / i)
    i = i + 1

tổng = int(tổng * 1000) / 1000
print("Kết quả bài 7:", tổng)