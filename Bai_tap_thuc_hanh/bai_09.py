so_kw = int(input("Nhập số KW điện tiêu thụ: "))

if so_kw <= 100:
    don_gia = 2000
elif 101 <= so_kw <= 200:
    don_gia = 2500
elif 201 <= so_kw <= 300:
    don_gia = 3000
else:
    don_gia = 5000

tien_dien = so_kw * don_gia
print(f"Tiền điện phải trả là: {tien_dien} đồng")
