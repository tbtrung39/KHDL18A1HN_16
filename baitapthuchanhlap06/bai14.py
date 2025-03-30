mật_khẩu = input("Nhập mật khẩu: ")
hợp_lệ = True
if not (6 <= len(mật_khẩu) <= 12):
    hợp_lệ = False
else:
    chữ_thường = False
    chữ_hoa = False
    chữ_số = False
    ký_tự_đặc_biệt = False

    for ký_tự in mật_khẩu:
        if 'a' <= ký_tự <= 'z':
            chữ_thường = True
        elif 'A' <= ký_tự <= 'Z':
            chữ_hoa = True
        elif '0' <= ký_tự <= '9':
            chữ_số = True
        elif ký_tự in ['$','#','@']:
            ký_tự_đặc_biệt = True
    if not (chữ_thường and chữ_hoa and chữ_số and ký_tự_đặc_biệt):
        hợp_lệ = False
if hợp_lệ:
    print("Mật khẩu hợp lệ")
else:
    print("Mật khẩu không hợp lệ")