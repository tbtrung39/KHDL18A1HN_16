ky_tu = input("Nhập một ký tự: ")  
while len(ky_tu) != 1:  
    print("Vui lòng nhập đúng 1 ký tự.")  
    ky_tu = input("Nhập một ký tự: ")  
gia_tri_ascii = ord(ky_tu)  
print("Giá trị ASCII của", ky_tu, "là", gia_tri_ascii)