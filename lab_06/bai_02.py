n=int(input("Nhap so luong so phan tu cua danh sach: "))
a=list(map(int,input(f"Nhap danh sach gom {n} phan tu ").split()))[:n]
print(a)
sx=sorted(set(a),reverse=True)
if len(sx)>1:
    print("Phan tu lon thu hai cua danh sach la:",sx[1])
    print("Va vi tri cua phan tu do la:",a.index(sx[1]))
else:
    print("Khong co phan tu lon thu hai")

dai_max=dai_ht=0
for so in a:
    if so>0:
        dai_ht+=1
        dai_max=max(dai_max,dai_ht)
    else:
        dai_ht=0
print("So luong cac so duong lien tiep nhieu nhat la:",dai_max)

tong_max=tong_ht=d=max_d=0
for so in a:
    if so>0:
        tong_ht+=so
        d+=1
        if tong_ht>tong_max:
            tong_max=tong_ht
            max_d=d
        else:
            tong_ht=d=0
print("So luong cac so duong lien tiep co tong lon nhat la: ",max_d)
