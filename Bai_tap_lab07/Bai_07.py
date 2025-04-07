import random
import string

A = set(random.choices(string.ascii_letters + string.digits, k=10))
B = set(random.choices(string.ascii_letters + string.digits, k=10))

print("Tập hợp A:", A)
print("Tập hợp B:", B)
print("Các phần tử chung của A và B:", A & B)