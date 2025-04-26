def ucln(a, b):
    if b == 0:
        return abs(a)
    else:
        return ucln(b, a % b)

def ucln_day_so(arr, n):
    if n == 1:
        return arr[0]
    else:
        return ucln(arr[n - 1], ucln_day_so(arr, n - 1))
n = int(input("Nhập số lượng phần tử: "))
arr = []

for i in range(n):
    so = int(input(f"Nhập số thứ {i + 1}: "))
    arr.append(so)

kq = ucln_day_so(arr, n)
print("Ước chung lớn nhất của dãy là:", kq)
