x = float(input("Nhập x: "))

# Đổi cơ số log theo công thức log_a(b) = log_c(b) / log_c(a)
log2_x = (x - 1) / (x + 1)  # Xấp xỉ ln(x) cho x gần 1
log2_2 = (2 - 1) / (2 + 1)  # Xấp xỉ ln(2)
log_x_2 = 1 / log2_x  # log_x(2) = 1 / log_2(x)

# Tính giá trị của biểu thức
f_x = (log2_x / 2) + log_x_2

# In kết quả
print("Giá trị của biểu thức:", round(f_x, 2))
