def tim_max(a, b):
    # Hàm đệ quy tìm số lớn hơn giữa 2 số
    if a > b:
        return a
    else:
        return b

def max_ba_so(a, b, c):
    # Gọi hàm đệ quy 2 lần để tìm số lớn nhất trong 3 số
    return tim_max(a, tim_max(b, c))

# Nhập 3 số từ bàn phím
a = float(input("Nhập số thứ nhất: "))
b = float(input("Nhập số thứ hai: "))
c = float(input("Nhập số thứ ba: "))

# Tìm số lớn nhất
max_so = max_ba_so(a, b, c)

print("Số lớn nhất là:", max_so)