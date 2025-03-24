Str1 = input("Nhap chuoi Str1: ")
tu = ""
for kytu in Str1:
    if kytu != ' ' and kytu != ',':
        tu += kytu
    else:
        if tu:
            print(tu)
            tu = ""
if tu:
    print(tu)