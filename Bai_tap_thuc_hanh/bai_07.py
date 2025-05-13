def tim_max_min(a, b, c):
    return max(a, b, c), min(a, b, c)

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
c = int(input("Nhập số thứ ba: "))

lon_nhat, nho_nhat = tim_max_min(a, b, c)
print("Số lớn nhất là:", lon_nhat)
print("Số nhỏ nhất là:", nho_nhat)
