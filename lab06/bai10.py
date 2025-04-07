import random

# Sinh một số ngẫu nhiên chia hết cho 5 và 7 trong khoảng từ 0 đến 200
valid_numbers = [num for num in range(0, 201) if num % 5 == 0 and num % 7 == 0]

# Chọn một số ngẫu nhiên từ danh sách valid_numbers
random_number = random.choice(valid_numbers)

print("Số ngẫu nhiên chia hết cho 5 và 7:", random_number)