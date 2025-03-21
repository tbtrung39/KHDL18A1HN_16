n = int(input("Nhập số: "))
np = ""
while n > 0:
    np = str(n % 2) + np
    n //= 2
print("Dạng nhị phân:", np)