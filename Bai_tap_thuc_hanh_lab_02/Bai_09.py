kw = float(input("Nhập số kw tiêu thụ: "))
if 0 <= kw <= 100:
    tien_dien = kw*2000
    print(f"Tiền điện là: {tien_dien}")
elif 101 <= kw <= 200:
    tien_dien = kw*2500
    print(f"Tiền điện là: {tien_dien}")
elif 201 <= kw <= 300:
    tien_dien = kw*3000
    print(f"Tiền điện là: {tien_dien}")
else:
    tien_dien = kw*5000
    print(f"Tiền điện là: {tien_dien}")