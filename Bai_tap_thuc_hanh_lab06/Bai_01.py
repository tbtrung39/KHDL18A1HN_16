a = [2,-2,1,9,-3,6,-2,6,-8]
# tính tổng các phần tử trong lst:
tong = 0
for i in a:
    tong += i
print(tong)
# đếm số hạng dương và tổng của chúng:
tong_duong = 0
dem = 0
for k in a:
    if k > 0:
        tong_duong += k
        dem += 1
print(f"Có {dem} số dương và tổng của chúng là: {tong_duong}")
# Tìm vị trí phần tử am đầu tiên trong lst:
for j in a:
    if j < 0:
        print(f"Vtri Phần tử âm đầu tiên trong lst là: {a.index(j)}")
        break
# Tìm vtri phần tử dương cuối cùng trong ds:
lst = [-10, -20, 30, -40, 50, -60]

# Duyệt từ phải sang trái để tìm số dương cuối cùng
for h in range(len(a) - 1, -1, -1):
    if a[h] > 0:
        print(f"Chỉ số của số dương cuối cùng ({a[h]}) là: {h}")
        break
# Tìm phần tử lớn nhất của ds và vị trí phần lớn nhất cuối cùng
max_a = max(a)
print(f"Phần tử lớn nhất ds {max_a} và vtr {a.index(max_a)}")


