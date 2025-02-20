# Nhập vận tốc ban đầu
a = float(input("Nhập vận tốc ban đầu của ô tô: "))

# Tính log_4(5) theo công thức log_4(5) = log_10(5) / log_10(4)
log_4_5 = (5 / 10) / (4 / 10)

# Tính thời gian t
t = a**4 / log_4_5

# In kết quả làm tròn đến 2 chữ số thập phân
print("Thời gian ô tô đi cho đến khi dừng lại:", round(t, 2))
