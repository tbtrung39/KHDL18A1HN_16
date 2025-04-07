# Khai báo tập hợp A
A = {1, 2.5, "hello", 3, "world", 4.0, "123", 5, 6.7}

# Khởi tạo biến đếm
count_int = 0
count_float = 0
count_str = 0

# Duyệt qua các phần tử trong tập hợp A
for element in A:
    if isinstance(element, int):   # Kiểm tra phần tử có phải là số nguyên không
        count_int += 1
    elif isinstance(element, float): # Kiểm tra phần tử có phải là số thực không
        count_float += 1
    elif isinstance(element, str):  # Kiểm tra phần tử có phải là chuỗi ký tự không
        count_str += 1

# In kết quả
print(f"Số lượng số nguyên trong tập hợp A: {count_int}")
print(f"Số lượng số thực trong tập hợp A: {count_float}")
print(f"Số lượng chuỗi ký tự trong tập hợp A: {count_str}")