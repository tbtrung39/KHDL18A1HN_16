# Nhập số phần tử n và danh sách các số tự nhiên
n = int(input("Nhập số phần tử n: "))
lst = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(num)

# Yêu cầu 1: Tìm phần tử lớn thứ hai và vị trí của nó
largest = second_largest = float('-inf')
second_largest_index = -1

# Duyệt qua danh sách để tìm phần tử lớn nhất và lớn thứ hai
for i in range(n):
    if lst[i] > largest:
        second_largest = largest
        largest = lst[i]
    elif lst[i] > second_largest and lst[i] != largest:
        second_largest = lst[i]
        second_largest_index = i

if second_largest != float('-inf'):
    print(f"Phần tử lớn thứ hai là: {second_largest}, Vị trí của nó là: {second_largest_index}")
else:
    print("Không có phần tử lớn thứ hai.")

# Yêu cầu 2: Tính số lượng các số dương liên tiếp nhiều nhất
max_streak = 0
current_streak = 0

for i in range(n):
    if lst[i] > 0:
        current_streak += 1
        max_streak = max(max_streak, current_streak)
    else:
        current_streak = 0

print(f"Số lượng các số dương liên tiếp nhiều nhất là: {max_streak}")

# Yêu cầu 3: Tính số lượng các số dương liên tiếp có tổng lớn nhất
max_sum = 0
current_sum = 0
max_streak_sum = 0

for i in range(n):
    if lst[i] > 0:
        current_sum += lst[i]
        max_streak_sum += 1
    else:
        if current_sum > max_sum:
            max_sum = current_sum
            current_streak_sum = max_streak_sum
        current_sum = 0
        max_streak_sum = 0

# Kiểm tra sau vòng lặp nếu chuỗi dương kết thúc ở cuối danh sách
if current_sum > max_sum:
    max_sum = current_sum
    current_streak_sum = max_streak_sum

print(f"Số lượng các số dương liên tiếp có tổng lớn nhất là: {current_streak_sum}, Tổng của chúng là: {max_sum}")
