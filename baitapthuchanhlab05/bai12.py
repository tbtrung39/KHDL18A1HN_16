str1 = input("Nhập chuỗi Str1: ")

tu = ""
for ky_tu in str1:
    if ky_tu != ' ' and ky_tu != ',':
        tu += ky_tu
    else:
        if tu:
            print(tu)
            tu = ""

if tu:
    print(tu)