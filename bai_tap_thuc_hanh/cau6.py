import random

# Nhập số tự nhiên n
n = int(input("Nhập số tự nhiên n: "))

# Tạo dãy A = [1, 2, ..., n]
A = list(range(1, n + 1))

# Khởi tạo danh sách kết quả
result = []

# Lấy ngẫu nhiên từng phần tử từ A và đưa vào result
while A:
    i = random.randint(0, len(A) - 1)  # Chọn chỉ số ngẫu nhiên
    result.append(A[i])               # Thêm phần tử vào kết quả
    A.pop(i)                          # Xóa phần tử khỏi A

# In kết quả
print("Hoán vị ngẫu nhiên:", result)