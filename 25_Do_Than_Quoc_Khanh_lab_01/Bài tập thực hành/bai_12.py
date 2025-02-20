import math
a = float(input("Nhập vận tốc ban đầu của xe (a): "))
log4_5 = math.log2(5) / 2
t = (2 * a**4) / log4_5
print(f"Thời gian ô tô đi được cho đến lúc dừng: {t:.2f} giây")
