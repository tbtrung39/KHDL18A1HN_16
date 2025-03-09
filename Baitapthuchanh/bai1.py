n = int(input("Nhập n: "))
ket_qua = 1.0
mau = 3.0
for i in range(1, n + 1):
    tu = 2.0
    for j in range(i):
        tu = tu * (2 * (j + 1))
    ket_qua = ket_qua + tu / mau
    mau = mau + 2
print("Kết quả:", round(ket_qua, 3))