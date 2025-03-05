# Nhập một ký tự từ bàn phím
print("Nhập một ký tự:")
ky_tu = input()

# Lấy giá trị ASCII của ký tự (dùng vòng lặp để tìm)
ascii_value = 0
i = 0

while i < len(ky_tu):  # Đảm bảo chỉ lấy ký tự đầu tiên nếu nhập nhiều
    ascii_value = ord(ky_tu[i])  # Sử dụng vòng lặp để truy cập ký tự
    i += 1

# In kết quả
print("Giá trị ASCII của ký tự", ky_tu, "là:", ascii_value)