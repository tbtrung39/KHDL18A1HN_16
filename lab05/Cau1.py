#Câu 1
# #Cach1:
str = input("Nhap mot chuoi ky tu: ")
count = 0
for char in str:
    if '0' <= char <= '9':
        count += 1
print("So ky tu la so trong chuoi la:", count)
#Cach2:
str = input("Nhap mot chuoi ky tu: ")
c = 0
for char in str:
    if char.isdigit():
        c += 1
print("So ky tu trong chuoi la: ", c)