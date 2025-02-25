import math

# Nhập vận tốc a của xe
a = float(input("Nhập vận tốc của xe (a): "))

# Tính log_4(5)
log_4_5 = math.log(5) / math.log(4)

# Tính thời gian t
t = a / (4 * log_4_5)

# Làm tròn kết quả đến 2 chữ số thập phân
t_rounded = round(t, 2)

# In kết quả
print(f"Thời gian ô tô đi được cho đến lúc dừng là: {t_rounded} giây")
