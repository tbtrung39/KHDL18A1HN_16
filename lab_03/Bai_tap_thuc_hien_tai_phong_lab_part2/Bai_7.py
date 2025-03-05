# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Biến lưu tổng
tong = 0.0  

# Dùng vòng lặp for để tính tổng nghịch đảo
for i in range(1, n + 1):
    tong += 1 / i  # Cộng nghịch đảo của i vào tổng

# In kết quả (làm tròn 3 chữ số thập phân)
print("Tổng nghịch đảo của số nguyên đầu tiên là:", tong)