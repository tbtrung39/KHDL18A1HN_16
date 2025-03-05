# Nhập giá trị x (góc tính theo radian)
print("Nhập giá trị x (đơn vị radian):")
x = float(input())

# Khởi tạo biến
cos_x = 1  # Giá trị khởi đầu của cos(x)
term = 1   # Biến để lưu từng số hạng của chuỗi Taylor
n = 2      # Bắt đầu từ bậc 2 vì cos(x) = 1 - x^2/2! + ...
sai_so = 10**-4  # Sai số yêu cầu

# Tính cos(x) bằng công thức truy hồi
while abs(term) > sai_so:
    term = -term * (x**2) / (n * (n - 1))  # Công thức truy hồi
    cos_x += term
    n += 2  # Tăng bậc lên 2 mỗi lần

# In kết quả
print("Giá trị gần đúng của cos(", x, ") là:", cos_x)