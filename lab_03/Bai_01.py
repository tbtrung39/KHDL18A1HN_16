import math 
n = int(input("Nhap gia tri n: "))
ket_qua = 0
for i in range (1, n +1):
    tu_so = 2*i+1
    mau_so = 2*i+3
    tich = 1
    for j in range (2, i + 2):
        tich *= j/(j+1)
    ket_qua += (tu_so/mau_so)*tich
ket_qua =  round(ket_qua, 3)
print("Ket qua:", ket_qua)
