# 1. Nhập danh sách số tự nhiên cho đến khi nhập số 0
numbers = []
while True:
    num = int(input("Nhập số (nhập 0 để kết thúc): "))
    if num == 0:
        break
    numbers.append(num)

print("Danh sách ban đầu:", numbers)

# 2. Chuyển các số dương lên đầu danh sách
positives = [x for x in numbers if x > 0]  # Danh sách số dương
negatives = [x for x in numbers if x <= 0]  # Danh sách số không dương (bao gồm 0 nếu có)
sorted_numbers = positives + negatives  # Ghép số dương trước, số âm sau

print("Danh sách sau khi chuyển số dương lên đầu:", sorted_numbers)

# 3. Nhập số m từ bàn phím
m = int(input("Nhập số m để chèn vào danh sách: "))

# Chèn m vào đầu, cuối và vị trí thứ 5 (nếu danh sách đủ dài)
sorted_numbers.insert(0, m)  # Chèn vào đầu
sorted_numbers.append(m)  # Chèn vào cuối

if len(sorted_numbers) >= 5:
    sorted_numbers.insert(4, m)  # Chèn vào vị trí thứ 5 (chỉ số 4)

# 4. In danh sách sau khi chèn m
print("Danh sách sau khi chèn m:", sorted_numbers)