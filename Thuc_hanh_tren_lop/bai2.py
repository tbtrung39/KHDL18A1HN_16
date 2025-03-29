# Nhập số phần tử n
n = int(input("Nhập số phần tử của danh sách: "))
lst = list(map(int, input("Nhập các phần tử của danh sách (cách nhau bởi dấu cách): ").split()))

# 1. Tìm phần tử lớn thứ hai và vị trí của nó
first_max = second_max = -1
second_max_index = -1
for i in range(n):
    if lst[i] > first_max:
        second_max = first_max
        first_max = lst[i]
        second_max_index = i
    elif lst[i] > second_max and lst[i] != first_max:
        second_max = lst[i]
        second_max_index = i
print(f"Phần tử lớn thứ hai là: {second_max}, Vị trí: {second_max_index}")

# 2. Tính số lượng các số dương liên tiếp nhiều nhất
max_positive_count = 0
current_count = 0
for num in lst:
    if num > 0:
        current_count += 1
        max_positive_count = max(max_positive_count, current_count)
    else:
        current_count = 0
print(f"Số lượng các số dương liên tiếp nhiều nhất là: {max_positive_count}")

# 3. Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
max_sum_count = 0
for num in lst:
    if num > 0:
        current_sum += num
        current_count += 1
        if current_sum > max_sum:
            max_sum = current_sum
            max_sum_count = current_count
    else:
        current_sum = 0
        current_count = 0
print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là: {max_sum_count}")
