import math
a = float(input("Nhập vận tốc của xe ô tô: "))
t = (a**4) / (math.log(5) / math.log(4))
t = round(t, 2)
print("Thời gian xe đi được cho đến lúc dừng là:", t, "giây")