import math
a = float(input("Nhap van toc ban dau a: "))
log4_5 = math.log(5) / math.log(4)
t = a**4 / log4_5
print("Thoi gian xe di cho den khi dung lai la:", round(t, 2), "giay")