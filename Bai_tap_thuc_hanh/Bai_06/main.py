import doicoso2 as dc2
chuoi = input("Nhập chuỗi: ")
loc = dc2.loc_ky_tu(chuoi)
print("Chuỗi sau khi lọc:", loc)
print("Cơ số xác định:", dc2.xac_dinh_co_so(loc))
print("Từ nhị phân sang thập phân:", dc2.doi_sang_co_so_10(loc, 2))
print("Từ bát phân sang thập phân:", dc2.doi_sang_co_so_10(loc, 8))
print("Từ thập lục phân sang thập phân:", dc2.doi_sang_co_so_10(loc, 16))
