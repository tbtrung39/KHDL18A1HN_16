# Nhập n từ bàn phím
n = int(input("Nhập n: "))

# Biến lưu tổng
tong = 0

# Dùng vòng lặp for để tính tổng bậc 3
for i in range(1, n + 1):
    tong += i ** 3  # Cộng lũy thừa bậc 3 của i vào tổng

# In kết quả
print("Tổng bậc 3 của số nguyên đầu tiên là:", tong)