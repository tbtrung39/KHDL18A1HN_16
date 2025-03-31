import random

# Tạo danh sách các số từ 0 đến 200 chia hết cho 5 và 7 bằng list comprehension
numbers = [x for x in range(201) if x % 5 == 0 and x % 7 == 0]

# Chọn ngẫu nhiên một số từ danh sách
random_number = random.choice(numbers)

# In kết quả
print("Số ngẫu nhiên chia hết cho 5 và 7:", random_number)