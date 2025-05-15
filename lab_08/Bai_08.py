import math

def tinh_chu_vi(r):
    return 2 * math.pi * r

def tinh_dien_tich(r):
    return math.pi * r ** 2

r = float(input("Nhập bán kính hình tròn: "))

if r <= 0:
    print("Bán kính phải lớn hơn 0.")
else:
    chu_vi = tinh_chu_vi(r)
    dien_tich = tinh_dien_tich(r)

    print(f"Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")
