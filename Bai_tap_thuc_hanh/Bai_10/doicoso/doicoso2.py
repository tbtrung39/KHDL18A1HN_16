def loc_ky_tu(s):
    s = s.upper()
    return ''.join(c for c in s if c.isdigit() or c in 'ABCDEF')

def xac_dinh_co_so(s):
    s = s.upper()
    if all(c in '01' for c in s):
        return 2
    elif all(c in '01234567' for c in s):
        return 8
    elif all(c in '0123456789' for c in s):
        return 10
    elif all(c in '0123456789ABCDEF' for c in s):
        return 16
    return -1

def doi_sang_thap_phan(s, base):
    try:
        return int(s, base)
    except:
        return "Không hợp lệ"
