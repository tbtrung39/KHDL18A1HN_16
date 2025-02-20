so = int(input("Nhập vào số nguyên có ba chữ số: "))
hang_tram = so // 100
hang_chuc = (so // 10) % 10
hang_dv = so % 10
chu_so = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
cach_doc = ""
cach_doc += chu_so[hang_tram] + " trăm"
if hang_chuc == 0 and hang_dv != 0:
    cach_doc += " linh"
elif hang_chuc == 1:
    cach_doc += " mười"
elif hang_chuc > 1:
    cach_doc += " " + chu_so[hang_chuc] + " mươi"

if hang_dv != 0:
    if hang_chuc > 1 and hang_dv == 1:
        cach_doc += " mốt"
    elif hang_chuc > 0 and hang_dv == 5:
        cach_doc += " lăm"
    else:
        cach_doc += " " + chu_so[hang_dv]
print("Cách đọc:", cach_doc)
