x = float(input("Nhập x (đơn vị radian): "))
sai_so = 10**-4  
cos_x = 1  
so_hang = 1  
n = 2  
while abs(so_hang) > sai_so:
    so_hang = (-so_hang * x * x) / (n * (n - 1))
    cos_x = cos_x + so_hang
    n = n + 2
print("cos(x) =", cos_x)
