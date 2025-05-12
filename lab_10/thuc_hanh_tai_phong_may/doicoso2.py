# doicoso2.py

def loc_ky_tu_hop_le(s):
    hop_le = set("0123456789ABCDEF")
    s = s.upper()
    ket_qua = ''.join([c for c in s if c in hop_le])
    return ket_qua

def xac_dinh_co_so(s):
    s = s.upper()
    if all(c in '01' for c in s):
        return 2
    elif all(c in '01234567' for c in s):
        return 8
    elif all(c in '0123456789ABCDEF' for c in s):
        return 16
    else:
        return -1  # Không xác định được

def co_so_2_sang_10(s):
    return int(s, 2)

def co_so_8_sang_10(s):
    return int(s, 8)

def co_so_16_sang_10(s):
    return int(s, 16)