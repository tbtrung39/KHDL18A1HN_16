def ucln(a, b):
    if b == 0:
        return a
    else:
        return ucln(b, a % b)

def ucln_day(lst, n):
    if n == 1:
        return lst[0]
    else:
        return ucln(lst[n-1], ucln_day(lst, n-1))

# Nhập n số từ bàn phím
n = int(input("Nhập số lượng phần tử: "))
lst = []
for i in range(n):
    x = int(input(f"Nhập số thứ {i+1}: "))
    lst.append(x)

# Tính ƯCLN của dãy số
ket_qua = ucln_day(lst, n)
print("Ước chung lớn nhất là:", ket_qua)
