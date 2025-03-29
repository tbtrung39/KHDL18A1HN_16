a = [2, -4, 1, 9, -3, 6, 3, -2, 6, 81]
# 1. Tính tổng các phần tử của danh sách
total_sum = sum(a)
print(f"Tổng các phần tử của danh sách: {total_sum}")

# 2. Đếm số lượng các số hạng dương và tổng của các số hạng dương
positive_numbers = [num for num in a if num > 0]
positive_count = len(positive_numbers)
positive_sum = sum(positive_numbers)
print(f"Số lượng các số hạng dương: {positive_count}")
print(f"Tổng các số hạng dương: {positive_sum}")

# 3. Tìm vị trí của phần tử âm đầu tiên trong danh sách
first_negative_index = next((i for i, num in enumerate(a) if num < 0), None)
if first_negative_index is not None:
    print(f"Vị trí của phần tử âm đầu tiên: {first_negative_index}")
else:
    print("Không có phần tử âm trong danh sách.")

# 4. Tìm vị trí của phần tử dương cuối cùng trong danh sách
last_positive_index = next((i for i in range(len(a)-1, -1, -1) if a[i] > 0), None)
if last_positive_index is not None:
    print(f"Vị trí của phần tử dương cuối cùng: {last_positive_index}")
else:
    print("Không có phần tử dương trong danh sách.")

# 5. Tìm phần tử lớn nhất của danh sách và vị trí phần tử lớn nhất cuối cùng
max_value = max(a)
max_value_last_index = len(a) - 1 - a[::-1].index(max_value)
print(f"Phần tử lớn nhất: {max_value}")
print(f"Vị trí của phần tử lớn nhất cuối cùng: {max_value_last_index}")
