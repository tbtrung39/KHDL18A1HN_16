bat_dau=int(input("Nhap gio bat dau: "))
ket_thuc=int(input("Nhap gio bat dau: "))
if 5<=bat_dau<=ket_thuc<=22:
    tong_gio = ket_thuc - bat_dau
    gia_3h_dau=100000
    gia_sau_3h=gia_3h_dau*0.75
    if tong_gio<=3:
        tien=tong_gio*gia_3h_dau
    else:
        tien=3*gia_3h_dau + (tong_gio-3)*gia_sau_3h
    if bat_dau>=11 and ket_thuc<=15:
        tien*=0.9
    print("So tien can phai tra la: ",tien)
else:
    print("Gio nhap khong hop le, vui long nhap lai")