# Nhập số nguyên n
n = int(input("Nhập số nguyên n: "))

# Khởi tạo dictionary rỗng
ket_qua = {}

# Duyệt từ 1 đến n và thêm vào dictionary
for i in range(1, n + 1):
    ket_qua[i] = i * i

# In kết quả
print(ket_qua)