so = int(input("Nhap so nguyen duong: "))
kq = ""
while so > 0:
    kq = chr(so % 2 + 48) + kq
    so //= 2
print("So nhi phan la:", kq)