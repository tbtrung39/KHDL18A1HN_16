gio_bat_dau=int(input("Nhập giờ bắt đầu:"))
gio_ket_thuc=int(input("Nhập giờ kết thúc:"))

if gio_bat_dau < 5 or gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc:
    print("Giờ nhập không hợp lệ!")
else:
    so_gio=gio_ket_thuc - gio_bat_dau
    tien_thue=0

    if so_gio <= 3:
        tien_thue=so_gio*100000
    else:
        tien_thue=3*100000
        tien_thue+=(so_gio-3)*100000*0.75

    if gio_bat_dau < 15 and gio_ket_thuc > 11:
        tien_thue*=0.9

    print("Số tiền phải trả là:",int(tien_thue),"đồngđồng")