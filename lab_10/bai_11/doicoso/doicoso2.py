def loc_ky_tu_hop_le(s):
    tap_hop = "0123456789ABCDEF"
    s = s.upper()
    ket_qua = "".join([k for k in s if k in tap_hop])
    print(f"Chuoi hop le: {ket_qua}")
    return ket_qua

def xac_dinh_co_so(s):
    s = s.upper()
    max_ky_tu = max(s)
    if max_ky_tu in "ABCDEF":
        return 16
    elif max_ky_tu in "89":
        return 10
    elif max_ky_tu in "8":
        return 9
    elif max_ky_tu in "01234567":
        return 8
    elif max_ky_tu in "01":
        return 2
    else:
        return "Khong xac dinh"

def nhi_phan_sang_thap_phan(s):
    return int(s, 2)

def bat_phan_sang_thap_phan(s):
    return int(s, 8)

def thap_luc_phan_sang_thap_phan(s):
    return int(s, 16)