def ucln(a, b):
    if b == 0:
        return a
    return ucln(b, a % b)

def ucln_day(danh_sach, n):
    if n == 1:
        return danh_sach[0]
    return ucln(danh_sach[n - 1], ucln_day(danh_sach, n - 1))

# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử: "))
day_so = []
for i in range(n):
    x = int(input(f"Nhập phần tử thứ {i+1}: "))
    day_so.append(x)

print("Ước chung lớn nhất của dãy là:", ucln_day(day_so, n))