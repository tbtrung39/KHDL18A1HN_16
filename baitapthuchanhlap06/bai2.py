n = int(input("Nhập số lượng phần tử: "))  
danh_sach = []  
for i in range(n):  
    danh_sach.append(int(input(f"Nhập phần tử thứ {i+1}: ")))  

count = 0 
for _ in danh_sach:  
    count += 1 

if count < 2:  
    print("Không đủ phần tử để tìm lớn thứ hai.")  
else:
    lon_nhat = max(danh_sach[0], danh_sach[1])  
    lon_thu_hai = min(danh_sach[0], danh_sach[1])  

    for i in range(2, count):  
        if danh_sach[i] > lon_nhat:
            lon_thu_hai = lon_nhat  
            lon_nhat = danh_sach[i]  
        elif danh_sach[i] > lon_thu_hai and danh_sach[i] != lon_nhat:  
            lon_thu_hai = danh_sach[i]  

    if lon_thu_hai is None:  
        print("Tất cả phần tử bằng nhau.")  
    else:
        vi_tri = count - 1 - danh_sach[::-1].index(lon_thu_hai)  
        print("Phần tử lớn thứ hai:", lon_thu_hai)  
        print("Vị trí phần tử lớn thứ hai:", vi_tri) 

so_luong_duong_lien_tiep_lon_nhat = 0 
tong_cac_so_duong_lien_tiep_lon_nhat = 0  
so_luong_duong_lien_tiep_hien_tai = 0  
tong_cac_so_duong_lien_tiep_hien_tai = 0 

for so in danh_sach:  
    if so > 0:  
        so_luong_duong_lien_tiep_hien_tai += 1  
        tong_cac_so_duong_lien_tiep_hien_tai += so  
        so_luong_duong_lien_tiep_lon_nhat = max(so_luong_duong_lien_tiep_lon_nhat, so_luong_duong_lien_tiep_hien_tai)  
        tong_cac_so_duong_lien_tiep_lon_nhat = max(tong_cac_so_duong_lien_tiep_lon_nhat, tong_cac_so_duong_lien_tiep_hien_tai) 
        so_luong_duong_lien_tiep_hien_tai = 0  
        tong_cac_so_duong_lien_tiep_hien_tai = 0  

print("Số lượng số dương liên tiếp nhiều nhất:", so_luong_duong_lien_tiep_lon_nhat)  
print("Tổng lớn nhất của số dương liên tiếp:", tong_cac_so_duong_lien_tiep_lon_nhat)  
