import math
x = float(input("Nhap gia tri x: "))
tu_so = -x + math.sqrt(x**2 + 4)
mau_so = math.sqrt(x**4 + 1)
ket_qua = tu_so / mau_so
print(f"Gia tri cua bieu thuc: {ket_qua:.2f}")