so_du = 0 
while True:
    giao_dich = input("Nhập giao dịch (D đẻ gửi ,W để rút ,Enter để kết thúc):").strip()
    if giao_dich =="":
        break
    parts=giao_dich.split()
    if len(parts) != 2 or not parts[1].isdigit():
        print("Sai định dạng")
        continue
    loai,so_tien = parts[0],int(parts[1])
    if loai == "D":
        so_du+= so_tien
    elif loai == "W":
        so_du -= so_tien
    else:
        print("Lệnh không hợp lệ")
print("Số dư tài khoản:",so_du)