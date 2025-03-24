str1=input("Nhap chuoi ky tu 1: ")
str2=input("Nhap chuoi ky tu 2: ")
mix=""
for i in range(max(len(str1),len(str2))):
    if i<len(str1):
        mix+=str1[i]
    if i<len(str2):
        mix+=str2[i]
print("Chuoi tron:",mix)