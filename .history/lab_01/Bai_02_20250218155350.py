s, m, h, d = map(input('Nhập giây, phút, giờ, ngày từ bàn phím: ').split())
tong_giay = d * 86400 + h * 3600 + m * 60 + s
print(f"Tổng số giây là {tong_giay}")

