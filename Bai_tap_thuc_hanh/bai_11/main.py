from doicoso import doicoso1, doicoso2

#doicoso1
n = int(input("Nhập số nguyên: "))
print("Hệ nhị phân:", doicoso1.chuyen_nhi_phan(n))
print("Hệ bát phân:", doicoso1.chuyen_bat_phan(n))
print("Hệ thập lục phân:", doicoso1.chuyen_thap_luc_phan(n))

#doicoso2
s = input("\nNhập chuỗi ký tự có thể chứa số: ")
chuoi_hop_le = doicoso2.loc_ky_tu_hop_le(s)
print("Chuỗi hợp lệ:", chuoi_hop_le)

coso = doicoso2.xac_dinh_co_so(chuoi_hop_le)
if coso == -1:
    print("Không xác định được cơ số.")
else:
    print("Chuỗi là cơ số:", coso)
    print("Chuyển sang hệ 10:", doicoso2.doi_sang_he_10(chuoi_hop_le, coso))
