# Bài 6: Tổng lũy thừa 3 của n số đầu tiên
n = int(input("Nhập n: "))
tổng = 0
i = 1
while i <= n:
    tổng = tổng + (i * i * i)
    i = i + 1
print("Kết quả bài 6:", tổng)