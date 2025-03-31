tien = 0
while True:
    nhap = input("Nhập giao dịch (hoặc bấm Enter để kết thúc): ").strip()
    if not nhap:
        break
    loai, so_tien = nhap.split()
    so_tien = int(so_tien)
    if loai == "D":
        tien += so_tien
    elif loai == "W":
        tien -= so_tien
print("Số dư tài khoản:", tien)