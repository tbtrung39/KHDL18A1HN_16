# Cau 4.

so_nguyen = int(input("Nhập vào một số nguyên: "))
so_nguyen = abs(so_nguyen)
so_nguyen_str = str(so_nguyen)
if len(so_nguyen_str) < 3:
    chu_so_hang_tram = 0
else:
    chu_so_hang_tram = so_nguyen_str[-3]  
print(f"Chữ số hàng trăm của số {so_nguyen} là: {chu_so_hang_tram}")