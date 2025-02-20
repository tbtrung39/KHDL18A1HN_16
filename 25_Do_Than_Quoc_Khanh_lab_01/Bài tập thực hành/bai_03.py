pi = 3.14 
ban_kinh = float(input("Nhập bán kính khối trụ: ")) 
chieu_cao = float(input("Nhập chiều cao khối trụ: ")) 
     
dien_tich_xq = round(2 * pi * ban_kinh * chieu_cao, 2) 
dien_tich_tp = round(dien_tich_xq + 2 * pi * ban_kinh**2, 2) 
the_tich = round(pi * ban_kinh**2 * chieu_cao, 2) 
print("\nKết quả tính toán khối trụ:") 
print(f"Diện tích xung quanh: {dien_tich_xq}") 
print(f"Diện tích toàn phần: {dien_tich_tp}") 
print(f"Thể tích: {the_tich}")