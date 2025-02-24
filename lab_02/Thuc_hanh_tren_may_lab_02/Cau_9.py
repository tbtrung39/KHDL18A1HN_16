# Nhập số kWh tiêu thụ
so_kw = int(input("Nhập số kWh điện tiêu thụ: "))

# Xác định đơn giá dựa trên số kWh tiêu thụ
if 0 <= so_kw <= 100:
    don_gia = 2000
elif 101 <= so_kw <= 200:
    don_gia = 2500
elif 201 <= so_kw <= 300:
    don_gia = 3000
else:  # so_kw > 300
    don_gia = 5000

# Tính tiền điện
tien_dien = so_kw * don_gia  

# Xuất kết quả
print("Tiền điện phải trả là:", tien_dien, "đồng")