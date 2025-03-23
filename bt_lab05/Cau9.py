# câu 9
# Cach1:
str = input("Nhập chuỗi ký tự: ")
max_char = ''
max_count = 0
for char in str:
    count = str.count(char)
    if count > max_count:
        max_count = count
        max_char = char
result = max_char * max_count
print("Chuỗi con dài nhất gồm các ký tự giống nhau là:", result)
# Cach2:
str = input("Nhập chuỗi ký tự: ")
chuoi_dai_nhat = ''
chuoi_hien_tai = ''
for i in range(len(str)):
    if i == 0 or str[i] == str[i - 1]:
        chuoi_hien_tai += str[i]
    else:
        if len(chuoi_hien_tai) > len(chuoi_dai_nhat):
            chuoi_dai_nhat = chuoi_hien_tai
        chuoi_hien_tai = str[i]
if len(chuoi_hien_tai) > len(chuoi_dai_nhat):
    chuoi_dai_nhat = chuoi_hien_tai
print("Chuỗi con dài nhất gồm các ký tự giống nhau là:", chuoi_dai_nhat)