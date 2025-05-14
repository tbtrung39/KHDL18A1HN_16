# Câu 3
def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)
a = float(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n (>= 0): "))
if n < 0:
    print("Chỉ hỗ trợ số mũ không âm.")
else:
    ket_qua = luy_thua(a, n)
print(f"{a}^{n} = {ket_qua}")