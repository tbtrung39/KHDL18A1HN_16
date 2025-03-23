chuoi_str = input("Nhập chuỗi Str: ")
chuoi_hex = ""
la_hex = True
for ky_tu in chuoi_str:
    if '0' <= ky_tu <= '9' or 'A' <= ky_tu <= 'F' or 'a' <= ky_tu <= 'f':
        chuoi_hex += ky_tu
    else:
        la_hex = False
if la_hex:
    thap_phan = 0
    for i in range(len(chuoi_hex)):
        if '0' <= chuoi_hex[i] <= '9':
            chu_so = ord(chuoi_hex[i]) - ord('0')
        elif 'A' <= chuoi_hex[i] <= 'F':
            chu_so = ord(chuoi_hex[i]) - ord('A') + 10
        else:
            chu_so = ord(chuoi_hex[i]) - ord('a') + 10
        thap_phan += chu_so * (16 ** (len(chuoi_hex) - 1 - i))
    print("Số thập phân tương ứng:", thap_phan)
else:
    print("Chuỗi Str không phải là chuỗi Hex.")