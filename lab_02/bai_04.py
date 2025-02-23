x = float(input("Nhập số thứ nhất: "))
y = float(input("Nhập số thứ hai: "))
if x > y or x == y:
    if x > y:
        print("Số lớn hơn là:", x)
    else:
        print("Hai số bằng nhau.")
else:
    print("Số lớn hơn là:", y)