ky_tu= input("Nhập một ký tự:")
while len(ky_tu) != 1:
    print("chỉ được nhập một kí tự:")
    ky_tu = input("Nhập một kí tự")
gia_tri_ascii = ord(ky_tu)
print("Giá trị ASCII cảu ký tự", ky_tu,"là:", gia_tri_ascii)