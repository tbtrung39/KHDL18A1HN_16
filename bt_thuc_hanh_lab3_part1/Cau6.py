# Câu 6
n = int(input("Nhập số n: "))
tong_bac_3 = 0
for i in range(1, n+1):
    tong_bac_3 += i ** 3
print("Tổng bậc 3 của {n} số nguyên đầu tiên là: {tong_bac_3}")