# Hàm đệ quy tính a^n
def luy_thua(a, n):
    if n == 0:
        return 1
    else:
        return a * luy_thua(a, n - 1)

# Nhập a và n từ bàn phím
a = float(input("Nhập cơ số a: "))
n = int(input("Nhập số mũ n: "))

# Gọi hàm và in kết quả
ket_qua = luy_thua(a, n)
print(f"{a}^{n} =", ket_qua)