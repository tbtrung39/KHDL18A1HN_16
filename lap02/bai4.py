so_nguyen = int(input("Nhập một số nguyên: "))

if so_nguyen >= 100:
    chu_so_hang_tram = (so_nguyen // 100) % 10
    print(f"Chữ số hàng trăm là: {chu_so_hang_tram}")
else:
    print("0")