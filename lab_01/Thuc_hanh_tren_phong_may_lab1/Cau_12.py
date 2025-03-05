import math

# Nhập vận tốc ban đầu a
a = float(input("Nhập vận tốc ban đầu của xe ô tô (m/s): "))

# Biểu thức vận tốc: v(t) = -t * log4(5) + a^4
log4_5 = math.log(5) / math.log(4)

# Khi xe dừng lại, v(t) = 0
# Giải phương trình: 0 = -t * log4(5) + a^4
thoi_gian_dung = a**4 / log4_5

# Làm tròn đến hai chữ số thập phân
thoi_gian_dung = round(thoi_gian_dung, 2)

# In kết quả
print(f"Thời gian ô tô đi cho đến lúc dừng: {thoi_gian_dung} giây")