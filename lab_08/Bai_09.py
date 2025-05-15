def cong(a, b):
    return a + b

def tru(a, b):
    return a - b

def nhan(a, b):
    return a * b

def chia(a, b):
    if b == 0:
        return "Lỗi: Không thể chia cho 0"
    return a / b

a = float(input("Nhập số thứ nhất (a): "))
b = float(input("Nhập số thứ hai (b): "))

print(f"{a} + {b} = {cong(a, b)}")
print(f"{a} - {b} = {tru(a, b)}")
print(f"{a} * {b} = {nhan(a, b)}")
ket_qua_chia = chia(a, b)
print(f"{a} / {b} = {ket_qua_chia}")
