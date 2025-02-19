h = int(input("Nhập số thời gian sử dụng bóng đèn(h): "))
giay = h *3600
tien_dien = (220*2.7*giay/1000)*7000
print(f"Tiền điện bạn phải trả là: {tien_dien}")