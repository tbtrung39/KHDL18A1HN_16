import math
a = float(input("Nhập vận tốc ban đầu (a): "))
t = a**4 / (math.log(5) / math.log(4))
t = round(t, 2)
print(f"Thời gian xe đi được: {t} giây")
