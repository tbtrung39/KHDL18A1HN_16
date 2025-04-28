def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    return max_of_three(b, c, a)
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
num3 = int(input("Nhập số thứ ba: "))
print("Số lớn nhất là:", max_of_three(num1, num2, num3))