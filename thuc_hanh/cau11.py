
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

so_duong_min = float('inf')
for num in a:
    if num > 0 and num < so_duong_min:
        so_duong_min = num

if so_duong_min == float('inf'):
    print("Không có số dương trong danh sách.")
else:
    print("Số dương nhỏ nhất trong danh sách là:", so_duong_min)
