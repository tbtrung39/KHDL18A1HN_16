import math
a = float(input("Nhập vận tốc ban đầu a (m/s): "))
log_4_5 = math.log(5) / math.log(4)
t = a / (4 * log_4_5)
print(f"Thời gian ô tô đi được cho đến lúc dừng là: {t:.2f} giây")