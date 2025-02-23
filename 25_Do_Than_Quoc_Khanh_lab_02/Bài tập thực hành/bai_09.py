kw = int(input("Nhập số kWh điện tiêu thụ: "))
if 0 <= kw <= 100:
    don_gia = 2000
elif 101 <= kw <= 200:
    don_gia = 2500
elif 201 <= kw <= 300:
    don_gia = 3000
elif kw > 300:
    don_gia = 5000
else:
    don_gia = 0
if don_gia > 0:
    tien_dien = kw * don_gia
    print("Đơn giá:", don_gia, "đồng/kWh")
    print("Tiền điện phải trả:", format(tien_dien, ",.0f"), "đồng")
else:
    print("Số kWh không hợp lệ! Vui lòng nhập số >= 0.")
