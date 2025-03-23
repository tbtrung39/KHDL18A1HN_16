#Cach1:
str1 = input("Nhập chuỗi thứ nhất: ")
str2 = input("Nhập chuỗi thứ hai: ")
do_dai_max = 0
chuoi_con_dai_nhat = ''
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        chuoi_con = str1[i:j]
        if chuoi_con in str2 and len(chuoi_con) > do_dai_max:
            do_dai_max = len(chuoi_con)
            chuoi_con_dai_nhat = chuoi_con
if chuoi_con_dai_nhat:
    print("Chuỗi con chung dài nhất là:", chuoi_con_dai_nhat)
else:
    print("Không có chuỗi con chung.")



#Cach2:
str1 = input("Nhập chuỗi ký tự 1: ")
str2 = input("Nhập chuỗi ký tự 2: ")
max_len = 0  
max_doan_chung = ""  

for i in range(len(str1)):
    for j in range(i, len(str1)):
        doan_con = str1[i:j+1]  
        if doan_con in str2 and len(doan_con) > max_len:  
            max_len = len(doan_con)
            max_doan_chung = doan_con
print("Đoạn ký tự chung dài nhất là:", max_doan_chung)