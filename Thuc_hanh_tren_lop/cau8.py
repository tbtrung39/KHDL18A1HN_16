import random
import string
A = set()
for _ in range(5):
    A.add(random.randint(-10, 10))
for _ in range(5):
    A.add(round(random.uniform(-10.0, 10.0), 2))
for _ in range(5):
    A.add(''.join(random.choices(string.ascii_letters, k=3))) 
integers = sum(1 for x in A if isinstance(x, int))
floats = sum(1 for x in A if isinstance(x, float))
strings = sum(1 for x in A if isinstance(x, str))
print(f"Tập hợp A: {A}")
print(f"Số phần tử là số nguyên: {integers}")
print(f"Số phần tử là số thực: {floats}")
print(f"Số phần tử là chuỗi ký tự: {strings}")