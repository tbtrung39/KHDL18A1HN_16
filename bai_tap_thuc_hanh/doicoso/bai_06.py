# main.py

import doi_co_so2
s = input("Nhập chuỗi ký tự: ")

chuoi_loc = doi_co_so2.loc_chuoi_hex(s)

coso = doi_co_so2.xac_dinh_co_so(chuoi_loc)
if coso:
    print(f"Chuỗi có thể thuộc cơ số: {coso}")
else:
    print("Không xác định được cơ số phù hợp.")

print("Chuyển từ nhị phân sang thập phân:", doi_co_so2.chuyen_co_so_2_sang_10(chuoi_loc))
print("Chuyển từ bát phân sang thập phân:", doi_co_so2.chuyen_co_so_8_sang_10(chuoi_loc))
print("Chuyển từ thập lục phân sang thập phân:", doi_co_so2.chuyen_co_so_16_sang_10(chuoi_loc))