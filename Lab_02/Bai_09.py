so_kw = int(input("Nhập số kWh điện tiêu thụ: "))

tien_dien = 0

if 0 <= so_kw <= 100:
    tien_dien = so_kw * 2000
elif 101 <= so_kw <= 200:
    tien_dien = 100 * 2000 + (so_kw - 100) * 2500
elif 201 <= so_kw <= 300:
    tien_dien = 100 * 2000 + 100 * 2500 + (so_kw - 200) * 3000
elif so_kw > 300:
    tien_dien = 100 * 2000 + 100 * 2500 + 100 * 3000 + (so_kw - 300) * 5000
else:
    print("Số kWh không hợp lệ!")
    tien_dien = None

if tien_dien is not None:
    print("Tiền điện phải trả:", tien_dien, "đồng")