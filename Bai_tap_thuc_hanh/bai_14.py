password = input("Nhập mật khẩu: ")

co_chu_thuong = False
co_chu_hoa = False
co_so = False
co_dac_biet = False
do_dai_hop_le = False

do_dai = 0
for ky_tu in password:
    do_dai += 1
    # Kiểm tra
    if ky_tu >= 'a' and ky_tu <= 'z':
        co_chu_thuong = True
    if ky_tu >= 'A' and ky_tu <= 'Z':
        co_chu_hoa = True
    if ky_tu >= '0' and ky_tu <= '9':
        co_so = True
    if ky_tu == '@' or ky_tu == '#' or ky_tu == '$':
        co_dac_biet = True

if do_dai >= 6 and do_dai <= 12:
    do_dai_hop_le = True

if co_chu_thuong and co_chu_hoa and co_so and co_dac_biet and do_dai_hop_le:
    print("Mật khẩu hợp lệ.")
else:
    print("Mật khẩu KHÔNG hợp lệ.")
