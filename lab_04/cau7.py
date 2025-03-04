a = int(input("Nhập số a: "))
b = int(input("Nhập số b: "))

m = a
n = b

while n != 0:
    m, n = n, m % n  # Tìm UCLN bằng thuật toán Euclid

bcnn = (a * b) // m
print("BCNN của", a, "và", b, "là", bcnn)
