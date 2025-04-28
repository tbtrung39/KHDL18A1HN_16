def dao_nguoc(n, kq=0):
    if n == 0:
        return kq
    else:
        kq = kq * 10 + n % 10  # Lấy chữ số cuối ghép vào kết quả
        return dao_nguoc(n // 10, kq)

# Nhập số từ bàn phím
n = int(input("Nhập số nguyên n: "))

# Gọi hàm và in kết quả
ket_qua = dao_nguoc(n)
print("Số đảo ngược là:", ket_qua)