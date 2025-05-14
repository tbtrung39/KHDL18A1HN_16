#cach1
str=input("Nhap chuoi ky tu: ")
dem=0
for so in str:
    if "0"<=so<="9":
        dem+=1
print("So ky tu la so trong chuoi ky tu tren la:",dem)

#cach2
d=0
for so in str:
    if so.isdigit():
        d+=1
print("So ky tu la so trong chuoi ky tu tren la:",d)