def lap_phuong(x):
    return x ** 3  # hoặc x * x * x

# Chương trình chính
n = int(input("Nhập một số nguyên: "))
ket_qua = lap_phuong(n)
print(f"Lập phương của {n} là: {ket_qua}")