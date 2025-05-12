import sys
sys.path.append("bai_11\doicoso")

import doicoso
so=doicoso.nhap_so()
doicoso.doi_nhi_phan(so)
doicoso.doi_bat_phan(so)
doicoso.doi_thap_luc_phan(so)

chuoi = input("Nhap chuoi ky tu: ")
chuoi_hop_le = doicoso.loc_ky_tu_hop_le(chuoi)

coso = doicoso.xac_dinh_co_so(chuoi_hop_le)
print(f"Chuoi bieu dien co so: {coso}")

if coso == 2:
    print("Chuyen sang he 10:", doicoso.nhi_phan_sang_thap_phan(chuoi_hop_le))
elif coso == 8:
    print("Chuyen sang he 10:", doicoso.bat_phan_sang_thap_phan(chuoi_hop_le))
elif coso == 16:
    print("Chuyen sang he 10:", doicoso.thap_luc_phan_sang_thap_phan(chuoi_hop_le))
else:
    print("Khong co ham chuyen doi tu co so do.")