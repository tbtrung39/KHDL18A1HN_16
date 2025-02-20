so_KW = float(input("Nhập vào số KW điện tiêu thụ: "))
if 0 <= so_KW <= 100:
    tien_dien = so_KW * 2000
elif 101 <= so_KW <= 200:
    tien_dien = 100 * 2000 + (so_KW - 100) * 2500
elif 201 <= so_KW <= 300:
    tien_dien = 100 * 2000 + 100 * 2500 + (so_KW - 200) * 3000
else:  # so_KW > 300
    tien_dien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (so_KW - 300) * 5000
print(f"Số tiền điện phải trả là: {tien_dien} đồng")
