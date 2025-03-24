hex = "0123456789ABCDEF"
chuoi = input("Nhập chuỗi: ").upper()
loc = ""
for c in chuoi:
    if c in hex:
        loc = loc + c

if len(loc) == len(chuoi):
    print("Hợp lệ Hex")
else:
    print("Đã lọc:", loc)

if len(loc) > 0:
    thap_phan = 0
    for c in loc:
        thap_phan = thap_phan * 16 + hex.index(c)
    print("Giá trị:", thap_phan)