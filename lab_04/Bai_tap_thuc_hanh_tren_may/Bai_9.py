# Nhập số nguyên từ bàn phím
print("Nhập một số nguyên:")
so = int(input())

# Đảm bảo số dương để dễ tính tổng chữ số
if so < 0:
    so = -so  # Lấy giá trị tuyệt đối nếu số âm

# Khởi tạo biến tổng
tong = 0

# Tính tổng các chữ số bằng vòng lặp while
while so > 0:
    tong += so % 10  # Lấy chữ số cuối cùng và cộng vào tổng
    so = so // 10  # Bỏ chữ số cuối cùng

# In kết quả
print("Tổng các chữ số là:", tong)