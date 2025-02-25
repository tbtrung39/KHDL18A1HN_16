kw = float(input("Nhập số KW điện tiêu thụ: "))
if kw >= 0 and kw <= 100:
    don_gia = 2000
elif kw > 100 and kw <= 200:
    don_gia = 2500
elif kw > 200 and kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000
tien_dien = kw * don_gia
print(f"Tiền điện phải trả là: {tien_dien} đồng")
