import random
import string
n = int(input("Nhập số lượng phần tử của mỗi tập hợp (A và B): "))
A = set(random.choices(string.ascii_letters + string.digits, k=n))
B = set(random.choices(string.ascii_letters + string.digits, k=n))
common_elements = A & B
print(f"Tập hợp A: {A}")
print(f"Tập hợp B: {B}")
print(f"Các phần tử chung của A và B: {common_elements}")
