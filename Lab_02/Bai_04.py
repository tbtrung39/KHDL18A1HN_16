so_nguyen = int(input("Nhập một số nguyên: "))

if so_nguyen < 100 and so_nguyen > -100:
    chu_so_hang_tram = 0
else:
    chu_so_hang_tram = abs(so_nguyen) // 100 % 10

print("Chữ số hàng trăm là:", chu_so_hang_tram)