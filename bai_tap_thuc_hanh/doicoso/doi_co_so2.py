def loc_chuoi_hex(s):
    s = s.upper()
    hop_le = '0123456789ABCDEF'
    ket_qua = ''.join([ch for ch in s if ch in hop_le])
    print(f"Chuỗi sau khi lọc: {ket_qua}")
    return ket_qua

def xac_dinh_co_so(s):
    s = s.upper()
    hop_le = {
        2: set('01'),
        8: set('01234567'),
        10: set('0123456789'),
        16: set('0123456789ABCDEF')
    }

    for base in [2, 8, 10, 16]:
        if all(ch in hop_le[base] for ch in s):
            return base
    return None

def chuyen_co_so_2_sang_10(s):
    try:
        return int(s, 2)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 2"

def chuyen_co_so_8_sang_10(s):
    try:
        return int(s, 8)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 8"

def chuyen_co_so_16_sang_10(s):
    try:
        return int(s, 16)
    except ValueError:
        return "Chuỗi không hợp lệ cho cơ số 16"