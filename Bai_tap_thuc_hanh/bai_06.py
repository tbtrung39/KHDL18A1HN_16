import random
lst = []
for _ in range(1000):
    lst.append(random.uniform(1.99999, 9.99999))
for i in range(len(lst) - 1):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print("Danh sách đã sắp xếp:", lst[:10], "...")