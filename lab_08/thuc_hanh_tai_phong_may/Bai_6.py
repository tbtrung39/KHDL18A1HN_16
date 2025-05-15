def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def bcnn(a, b):
    return abs(a * b) // ucln(a, b)

# Chương trình chính
a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))

ket_qua = bcnn(a, b)
print(f"Bội chung nhỏ nhất của {a} và {b} là: {ket_qua}")