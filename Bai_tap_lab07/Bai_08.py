import random
import string

A = {
    1, 2.5, "hello", 3, 4.2, "world",
    random.randint(1, 100),
    random.uniform(1, 100),
    ''.join(random.choices(string.ascii_letters, k=5))
}

int_count = sum(1 for item in A if isinstance(item, int))
float_count = sum(1 for item in A if isinstance(item, float))
str_count = sum(1 for item in A if isinstance(item, str))

print("Tập hợp A:", A)
print("Số phần tử là số nguyên:", int_count)
print("Số phần tử là số thực:", float_count)
print("Số phần tử là chuỗi ký tự:", str_count)