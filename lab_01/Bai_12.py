
a = float(input("Nhập vận tốc ban đầu của xe (a): "))
log_4_5 = 0.774
t = a**4 / log_4_5
t = round(t, 2)
print("Thời gian xe dừng lại là:", t, "giây")