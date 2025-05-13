from doicoso import doi_co_so1, doi_co_so2

print("=== Chuyển đổi từ số nguyên ===")
n = doi_co_so1.nhap_so()
print("Nhị phân:", doi_co_so1.doi_nhi_phan(n))
print("Bát phân:", doi_co_so1.doi_bat_phan(n))
print("Thập lục phân:", doi_co_so1.doi_thap_luc_phan(n))

print("\n=== Xử lý chuỗi cơ số ===")
s = input("Nhập chuỗi ký tự: ")
chuoi_loc = doi_co_so2.loc_chuoi_hex(s)
print("Chuỗi sau khi lọc:", chuoi_loc)

co_so = doi_co_so2.xac_dinh_co_so(chuoi_loc)
print("Chuỗi có thể là ở hệ cơ số:", co_so)

if co_so == 2:
    print("Sang hệ thập phân:", doi_co_so2.chuyen_co_so_2_sang_10(chuoi_loc))
elif co_so == 8:
    print("Sang hệ thập phân:",doi_co_so2.chuyen_co_so_8_sang_10(chuoi_loc))
elif co_so == 16:
    print("Sang hệ thập phân:", doi_co_so2.chuyen_co_so_16_sang_10(chuoi_loc))
else:
    print("Không thể chuyển đổi.")