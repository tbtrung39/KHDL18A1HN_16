# Danh sách đã cho
a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 8]

# 1. Tính tổng các phần tử trong danh sách
sum_all = sum(a)
print("Tổng các phần tử trong danh sách:", sum_all)

# 2. Đếm số lượng số dương và tính tổng số dương
positive_numbers = [x for x in a if x > 0]
count_positive = len(positive_numbers)
sum_positive = sum(positive_numbers)
print("Số lượng số dương:", count_positive)
print("Tổng các số dương:", sum_positive)

# 3. Tìm vị trí của phần tử âm đầu tiên
pos_first_negative = next((i for i, x in enumerate(a) if x < 0), -1)
print("Vị trí của phần tử âm đầu tiên:", pos_first_negative)

# 4. Tìm vị trí của phần tử dương cuối cùng
pos_last_positive = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), -1)
print("Vị trí của phần tử dương cuối cùng:", pos_last_positive)

# 5. Tìm phần tử lớn nhất và vị trí phần tử lớn nhất cuối cùng
max_value = max(a)
pos_last_max = len(a) - 1 - a[::-1].index(max_value)  # Tìm vị trí xuất hiện cuối cùng
print("Phần tử lớn nhất:", max_value)
print("Vị trí cuối cùng của phần tử lớn nhất:", pos_last_max)