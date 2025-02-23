kw = float(input("Nhập số KW tiêu thụ: "))

if kw <= 100:
    gia = kw * 2000
elif kw <= 200:
    gia = 100 * 2000 + (kw - 100) * 2500
elif kw <= 300:
    gia = 100 * 2000 + 100 * 2500 + (kw - 200) * 3000
else:
    gia = 100 * 2000 + 100 * 2500 + 100 * 3000 + (kw - 300) * 5000

print("Tiền điện phải trả:", gia, "VNĐ")