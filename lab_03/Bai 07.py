n = int(input("Nhap mot so: "))
tong_nghich_dao = 0
for i in range(1, n + 1):
    tong_nghich_dao += 1 / i
print(f"Tong nghich dao cua {n} so nguyen dau tien la {tong_nghich_dao}")