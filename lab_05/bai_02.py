#cach1
s=input("Nhap chuoi: ")
d=0
for kt in s:
    if not ("0"<=kt<="9" or "A"<=kt<="Z" or "a"<=kt<="z"):
        d+=1
print("So ky tu khong phai la chu cai tieng anh va khong la so trong chuoi tren la: ",d)
#cach2
c=0
for t in s:
    if not (t.isalpha() or t.isdigit()):
        c+=1
print("So ky tu khong phai la chu cai tieng anh va khong la so trong chuoi tren la:",c)