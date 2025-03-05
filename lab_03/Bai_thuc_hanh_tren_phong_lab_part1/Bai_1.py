# Nhập giá trị n từ người dùng
n = int(input("Nhập n: "))

# Biến tổng để lưu kết quả
tong = 1.0
# Biến tích để tính từng số hạng của dãy
tich = 1.0

# Vòng lặp để tính từng số hạng
for i in range(1, n+1):
    tich *= (2 * i) / (2 * i + 1)  # Nhân với phân số tiếp theo
    tong += tich  # Cộng vào tổng

# In kết quả, làm tròn 3 chữ số thập phân
print("Kết quả: %.3f" % tong)