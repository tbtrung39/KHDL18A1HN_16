def tim_so_nho_nhat(a, b, c):
    return min(a, b, c)

def tim_so_lon_nhat(a, b, c):
    return max(a, b, c)

a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))

nho_nhat = tim_so_nho_nhat(a, b, c)
lon_nhat = tim_so_lon_nhat(a, b, c)

print(f"Số nhỏ nhất là: {nho_nhat}")
print(f"Số lớn nhất là: {lon_nhat}")
