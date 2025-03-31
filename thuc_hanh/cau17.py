
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

tong_le = 0
for num in a:
    if num % 2 != 0:  
        tong_le += num

print("Tổng các phần tử lẻ trong danh sách là:", tong_le)
