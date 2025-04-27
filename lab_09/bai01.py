def find_max_recursive(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print("Nhập 3 số nguyên từ bàn phím.")
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))
num3 = int(input("Nhập số thứ ba: "))
max_number = find_max_recursive(num1, num2, num3)
print("Số lớn nhất trong ba số", num1, ",", num2, ",", num3, "là:", max_number)