def loc_ky_tu_hop_le(s):
    tap_hop = set('0123456789ABCDEF')
    s = s.upper()
    return ''.join([c for c in s if c in tap_hop])

def xac_dinh_he_co_so(s):
    s = s.upper()
    if all(c in '01' for c in s):
        return 2
    elif all(c in '01234567' for c in s):
        return 8
    elif all(c in '0123456789' for c in s):
        return 10
    elif all(c in '0123456789ABCDEF' for c in s):
        return 16
    else:
        return -1  

def doi_co_so_sang_10(s, base):
    try:
        return int(s, base)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số này"
