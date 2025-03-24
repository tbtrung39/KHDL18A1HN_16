st1 = input("Nhap chuoi: ")
tu = ""
print("Cac tu trong chuoi:")
for c in st1:
    if c != ' ' and c != ',':
        tu += c
    elif tu != "":
        print(tu)
        tu = ""
if tu != "":
    print(tu)