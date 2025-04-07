import random

# Tạo danh sách gồm các chữ số từ 0 đến 9
digits = list(range(10))

# Tạo tập hợp A gồm 5 phần tử ngẫu nhiên từ danh sách trên
A = set(random.sample(digits, 5))  # sample đảm bảo không trùng lặp

# In kết quả
print("Tập hợp A gồm 5 chữ số ngẫu nhiên:", A)