n = int(input("Nhap mot so nguyen duong: "))
while n <= 0:
    n = int(input("So khong hop le. Vui long nhap lai mot so nguyen duong: "))
so_goc = n
phan_tich = []
i = 2
while i <= n:
    while n % i == 0:
        phan_tich.append(i)
        n //= i
    i += 1
ket_qua = " * ".join(map(str, phan_tich))
print(f"Phan tich thua so nguyen to cua {so_goc} la: {ket_qua}")