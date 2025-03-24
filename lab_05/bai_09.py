chuoi = input("Nhap chuoi: ")

do_dai_max = 0
chuoi_max = ""
do_dai_hien_tai = 1

for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:  
        do_dai_hien_tai += 1  
    else:
        if do_dai_hien_tai > do_dai_max:
            do_dai_max = do_dai_hien_tai
            chuoi_max = chuoi[i - 1] * do_dai_hien_tai
        do_dai_hien_tai = 1  

if do_dai_hien_tai > do_dai_max:
    chuoi_max = chuoi[-1] * do_dai_hien_tai

print("Chuoi con dai nhat co cac ky tu giong nhau la:", chuoi_max)