a = float(input("Nhập vận tốc a của xe ô tô (m/s): "))
log4_5 = (5 ** 0.5) / (4 ** 0.5)  
t = a**4 / log4_5
t_rounded = round(t, 2)
print(f"Thời gian xe dừng lại là: {t_rounded} giây")
