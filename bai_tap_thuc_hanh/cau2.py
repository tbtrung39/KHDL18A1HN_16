import math

# Hàm đệ quy để tính ƯCLN của 2 số
def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

# Hàm đệ quy để tính ƯCLN của n số trong danh sách
def ucln_day_so(numbers, index=0):
    if len(numbers) == 1:
        return numbers[0]
    if index == len(numbers) - 1:
        return numbers[index]
    return ucln(numbers[index], ucln_day_so(numbers, index + 1))

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử: "))

# Nhập danh sách các số
numbers = []
for i in range(n):
    num = int(input(f"Nhập số thứ {i + 1}: "))
    numbers.append(num)

# Tính ƯCLN của n số
ket_qua = ucln_day_so(numbers)

print("Ước chung lớn nhất của dãy số là:", ket_qua)