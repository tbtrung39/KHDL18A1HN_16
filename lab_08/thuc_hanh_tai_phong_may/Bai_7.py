def tim_min(a, b, c):
    return min(a, b, c)

def tim_max(a, b, c):
    return max(a, b, c)

# Chương trình chính
a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

nho_nhat = tim_min(a, b, c)
lon_nhat = tim_max(a, b, c)

print(f"Số nhỏ nhất là: {nho_nhat}")
print(f"Số lớn nhất là: {lon_nhat}")