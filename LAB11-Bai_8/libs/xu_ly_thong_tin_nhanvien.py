def tinh_luong(he_so_luong):
    return he_so_luong * 1490000

def tinh_phu_cap(chuc_vu):
    chuc_vu = chuc_vu.upper()
    if chuc_vu == "TP":
        return 1000000
    elif chuc_vu == "PP":
        return 700000
    else:
        return 300000

def tinh_thuc_linh(he_so_luong, chuc_vu):
    return tinh_luong(he_so_luong) + tinh_phu_cap(chuc_vu)

def sap_xep_theo_thuc_linh(ds_nv):
    return sorted(ds_nv, key=lambda nv: nv["thuc_linh"], reverse=True)