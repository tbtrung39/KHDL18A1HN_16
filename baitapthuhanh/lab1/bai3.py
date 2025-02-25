r = float(input("Nhập bán kính: "))
h = float(input("Nhập chiều cao: "))
pi = 3.14
s_xq = 2 * pi * r * h
s_tp = 2 * pi * r * (r + h)
v = pi * r**2 * h
print(f"Diện tích xung quanh: {s_xq:.2f}, Tổng diện tích: {s_tp:.2f}, Thể tích: {v:.2f}")