# Câu 1
def max_recursive(a, b):
    if a > b:
        return a
    else:
        return b
def max_of_three(x, y, z):
    return max_recursive(max_recursive(x, y), z)
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))
max_number = max_of_three(a, b, c)
print("Số lớn nhất là:", max_number)