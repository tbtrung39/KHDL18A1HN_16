from doicoso import doicoso1, doicoso2

n = doicoso1.nhap_so()
print("Nhị phân:", doicoso1.nhi_phan(n))
print("Bát phân:", doicoso1.bat_phan(n))
print("Thập lục phân:", doicoso1.thap_luc_phan(n))

s = input("Nhập chuỗi số: ")
loc = doicoso2.loc_ky_tu(s)
print("Chuỗi hợp lệ:", loc)
coso = doicoso2.xac_dinh_co_so(loc)
print("Cơ số xác định:", coso)
if coso in [2, 8, 16]:
    print(f"Giá trị thập phân:", doicoso2.doi_sang_thap_phan(loc, coso))
