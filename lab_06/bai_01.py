a=[2,-4,1,9,-3,6,3,-2,6,8]
print("Cho danh sach a=[2,-4,1,9,-3,6,3,-2,6,8]")
tong=0
for i in a:
    tong+=i
print("Tong cac phan tu cua danh sach a la:",tong)

tong_duong=0
dem=0
for t in a:
    if t>0:
        dem+=1
        tong_duong+=t
print("So luong so hang duong trong danh sach la:",dem)
print(f"Tong cac so hang duong do la: {tong_duong}")

for j in range(len(a)):
    if a[j]<0:
        print("Vi tri cua phan tu am dau tien trong danh sach la:",j)
        break

for s in (len(a)-1,-1,-1):
    if a[s]>0:
        print("Vi tri cua phan tu duong cuoi cung trong danh sach la:",s)
        break

print("Phan tu lon nhat trong danh sach la:",max(a))
print("Vi tri cua phan tu lon nhat do la:",a.index(max(a)))