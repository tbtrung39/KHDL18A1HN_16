import random

n = int(input("Nhập số lượng số thực ngẫu nhiên n: "))
random_set = set()
count = 0
while count < n:
    random_number = random.uniform(0, 100)  
    random_set.add(random_number)
    count += 1

print("Set số thực ngẫu nhiên:", random_set)

min_val = None
max_val = None
total_sum = 0

first = True
for num in random_set:
    if first:
        min_val = num
        max_val = num
        first = False
    else:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    total_sum += num

print("Phần tử nhỏ nhất:", min_val)
print("Phần tử lớn nhất:", max_val)
print("Tổng các phần tử:", total_sum)