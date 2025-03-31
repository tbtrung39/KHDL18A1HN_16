import random

# Sinh danh sách A gồm 1000 số ngẫu nhiên từ 1 đến 99999
A = [random.randint(1, 99999) for _ in range(1000)]

# In danh sách (hiển thị 20 phần tử đầu tiên để kiểm tra)
print("Danh sách A:", A[:20], "...")