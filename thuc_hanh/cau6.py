import random

list_A = [random.randint(1, 99999) for _ in range(1000)]

sorted_asc = sorted(list_A)
sorted_desc = sorted(list_A, reverse=True)

print("Danh sách 1000 số đã sắp xếp tăng dần:", sorted_asc[:10], "...")  # In 10 số đầu để kiểm tra
print("Danh sách 1000 số đã sắp xếp giảm dần:", sorted_desc[:10], "...")
