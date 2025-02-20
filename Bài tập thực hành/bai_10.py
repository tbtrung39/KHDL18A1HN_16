ba_gio_dau=100000 
gia_giam=ba_gio_dau*0.75 
gio_bat_dau=int(input('Nhập giờ bắt đầu(từ 5-22):')) 
gio_ket_thuc=int(input('Nhập giò kết thúc(từ 5-22):')) 
if gio_bat_dau >=11 and gio_ket_thuc <= 15: 
    gio_giam_gia=0.10 
elif gio_bat_dau < 5 and gio_ket_thuc > 22 or gio_bat_dau >= gio_ket_thuc: 
    print('Giờ không hợp lệ') 
tong_so_gio=gio_ket_thuc-gio_bat_dau 
if tong_so_gio <= 3: 
    gia=tong_so_gio*ba_gio_dau 
else: 
    gia= 3*ba_gio_dau+(tong_so_gio-3)*gio_giam_gia 
if gio_bat_dau < 15 and gio_ket_thuc > 11: 
    gia = gia*gio_giam_gia 
print(f'Só tiền phải trả : {gia} đồng') 

 