# Yêu cầu 1: Nhập vào danh sách các phần tử số tự nhiên cho đến khi nhập vào số 0
lst = []

while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Yêu cầu 2: Chuyển các phần tử dương lên đầu danh sách
positive_nums = []
negative_nums = []

# Duyệt qua danh sách và tách phần tử dương và âm
for num in lst:
    if num > 0:
        positive_nums.append(num)
    else:
        negative_nums.append(num)

# Kết hợp lại: phần tử dương lên đầu, phần tử âm xuống sau
lst = positive_nums + negative_nums
print("Danh sách sau khi chuyển các phần tử dương lên đầu:", lst)

# Yêu cầu 3: Chèn một số m vào đầu, cuối và vị trí thứ 5 của danh sách
m = int(input("Nhập số m để chèn vào danh sách: "))

# 1. Chèn m vào đầu danh sách
lst = [m] + lst  # Tạo một danh sách mới với m là phần tử đầu tiên

# 2. Chèn m vào cuối danh sách
lst = lst + [m]  # Tạo một danh sách mới với m là phần tử cuối cùng

# 3. Chèn m vào vị trí thứ 5 nếu danh sách có ít nhất 5 phần tử
if len(lst) >= 5:
    lst = lst[:5] + [m] + lst[5:]  # Tạo một danh sách mới với m được chèn vào vị trí thứ 5

# In danh sách sau khi thực hiện các thao tác chèn
print("Danh sách sau khi chèn số m:", lst)
