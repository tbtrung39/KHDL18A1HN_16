def nhap_chuoi_so_hex():
    while True:
        chuoi_nhap = input("Vui lòng nhập một chuỗi số hệ 16 (0-9, A-F): ").upper()
        chuoi_hop_le = ""
        for char in chuoi_nhap:
            if '0' <= char <= '9' or 'A' <= char <= 'F':
                chuoi_hop_le += char
        if chuoi_hop_le:
            print(f"Chuỗi hợp lệ đã nhập: {chuoi_hop_le}")
            return chuoi_hop_le
        else:
            print("Lỗi: Chuỗi nhập không chứa ký tự hợp lệ nào. Vui lòng thử lại.")

def xac_dinh_co_so(chuoi_so):
    la_nhi_phan = all(char in '01' for char in chuoi_so)
    la_bat_phan = all(char in '01234567' for char in chuoi_so)
    la_thap_luc_phan = all(char in '0123456789ABCDEF' for char in chuoi_so)

    if la_thap_luc_phan:
        return 16
    elif la_bat_phan:
        return 8
    elif la_nhi_phan:
        return 2
    else:
        return None

def sang_decimal(chuoi_so, co_so):
    try:
        return int(chuoi_so, co_so)
    except ValueError:
        return None

if __name__ == "__main__":
    print("Đây là module doicoso2. Vui lòng chạy file chương trình chính để sử dụng.")