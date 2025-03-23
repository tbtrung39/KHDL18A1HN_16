chuoi_str = input("Nhập chuỗi Str: ")
chuoi_so = ""
for ky_tu in chuoi_str:
    if '0' <= ky_tu <= '9':
        chuoi_so += ky_tu
print("Chuỗi số sau khi xóa ký tự không phải số:", chuoi_so)

if chuoi_so:
    so = int(chuoi_so)
    tong_uoc = 1
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            tong_uoc += i
            if i != so // i:
                tong_uoc += so // i
    if tong_uoc == so:
        print("Chuỗi số này là số hoàn hảo.")
    else:
        print("Chuỗi số này không phải là số hoàn hảo.")
else:
    print("Chuỗi số không có số.")