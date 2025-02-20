import math

a = float(input("Nhập vận tốc ban đầu của ô tô (m/s): "))

t = 0
while (-t * math.log(4, 5) + (a / 4)) > 0:
    t += 0.01  

t = round(t, 2)
print("Thời gian ô tô đi được cho đến lúc dừng là:", t, "giây")