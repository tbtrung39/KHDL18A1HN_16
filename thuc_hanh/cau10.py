import random

random_list = [random.randint(0, 200) for _ in range(100)]
filtered_list = [x for x in random_list if x % 5 == 0 and x % 7 == 0]

print("Danh sách số ngẫu nhiên:", random_list)
print("Danh sách số chia hết cho 5 và 7:", filtered_list)
