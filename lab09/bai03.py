def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)
a = float(input("Nhập cơ số a:"))
n = int(input("NHập số mũ n:"))
ket_qua = luy_thua(a,n)
print(f"{a} mũ {n} là :", ket_qua)