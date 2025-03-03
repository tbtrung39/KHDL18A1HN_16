n = int(input("Nhap mot so nguyen duong: "))
while n <= 0:
    n = int(input("So khong hop le. Vui long nhap lai mot so nguyen duong: "))
# a)
S1 = n * (n + 1) // 2
print(f"S1 = 1 + 2 + 3 + ... + {n} = {S1}")
# b)
S2 = (n + 1) ** 2
print(f"S2 = 1 + 3 + 5 + ... + (2*{n}+1) = {S2}")
# c)
S3 = n * (n + 1)
print(f"S3 = 2 + 4 + 6 + ... + 2*{n} = {S3}")