#Cach1:
str1 = input("Nhập chuỗi ký tự Str1: ")
tu_tach = str1.replace(",", " ").split()
for tu in tu_tach:
    print(tu)



#Cach2:
str1 = input("Nhập chuỗi ký tự Str1: ")
tu_hien_tai = ""
for char in str1:
    if char != " " and char != ",":  
        tu_hien_tai += char  
    else:
        if tu_hien_tai: 
            print(tu_hien_tai) 
            tu_hien_tai = ""  
if tu_hien_tai:
    print(tu_hien_tai)