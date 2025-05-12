def loc_ky_tu_hop_le(s):
    hop_le = "0123456789ABCDEF"
    s = s.upper()
    ket_qua = "".join([c for c in s if c in hop_le])
    print("Chuỗi sau khi lọc:", ket_qua)
    return ket_qua

def co_so_nao(s):
    s = s.upper()
    if all(c in "01" for c in s):
        return 2
    elif all(c in "01234567" for c in s):
        return 8
    elif all(c in "0123456789ABCDEF" for c in s):
        return 16
    else:
        return -1

def nhi_phan_sang_thap_phan(s):
    return int(s, 2)

def bat_phan_sang_thap_phan(s):
    return int(s, 8)

def thap_luc_phan_sang_thap_phan(s):
    return int(s, 16)