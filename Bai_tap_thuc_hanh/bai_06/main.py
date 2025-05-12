import doicoso2

chuoi = input("Nhập chuỗi ký tự: ")
chuoi_sach = doicoso2.loc_ky_tu_hop_le(chuoi)
print(f"Chuỗi sau khi lọc: {chuoi_sach}")

co_so = doicoso2.xac_dinh_he_co_so(chuoi_sach)
if co_so == -1:
    print("Không xác định được hệ cơ số của chuỗi.")
else:
    print(f"Chuỗi được xác định ở cơ số: {co_so}")

print("Chuyển đổi từ các hệ sang cơ số 10:")
print("Từ cơ số 2:", doicoso2.doi_co_so_sang_10(chuoi_sach, 2))
print("Từ cơ số 8:", doicoso2.doi_co_so_sang_10(chuoi_sach, 8))
print("Từ cơ số 16:", doicoso2.doi_co_so_sang_10(chuoi_sach, 16))
