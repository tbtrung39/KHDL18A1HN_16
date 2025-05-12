import doicoso2

chuoi = input("Nhap chuoi ky tu: ")
chuoi_hop_le = doicoso2.loc_ky_tu_hop_le(chuoi)

coso = doicoso2.xac_dinh_co_so(chuoi_hop_le)
print(f"Chuoi bieu dien co so: {coso}")

if coso == 2:
    print("Chuyen sang he 10:", doicoso2.nhi_phan_sang_thap_phan(chuoi_hop_le))
elif coso == 8:
    print("Chuyen sang he 10:", doicoso2.bat_phan_sang_thap_phan(chuoi_hop_le))
elif coso == 16:
    print("Chuyen sang he 10:", doicoso2.thap_luc_phan_sang_thap_phan(chuoi_hop_le))
else:
    print("Khong co ham chuyen doi tu co so do.")