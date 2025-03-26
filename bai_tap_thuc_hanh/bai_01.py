a=[2,-4,1,9,-3,6,3,-2,6,8]
tong=sum(a)
print("Tổng các phần tử:",tong)
so_luong_duong = 0
tong_duong = 0
for x in a :
    if x > 0 :
        so_luong_duong +=1
        tong_duong +=x
print("Số luong số hạng dương:",so_luong_duong)
print("Tổng các số hạng dương:",tong_duong)
vi_tri_am_dau = -1
for i in range(len(a)):
    if a[i]<0:
        vi_tri_am_dau = i 
        break
print("Vị trí phần tử âm đầu tiên :",vi_tri_am_dau)
vi_tri_duong_cuoi = -1
for i in range(len(a)-1,-1,-1):
    if a[i] > 0 :
        vi_tri_duong_cuoi = i
        break
print("Vị trí phần tử âm đầu tiên:",vi_tri_duong_cuoi)
max_value = max(a)
vi_tri_max_cuoi = -1
for i in range(len(a)-1,-1,-1):
    vi_tri_max_cuoi= i
    break
print("phần tử lớn nhất:",max_value)
print("Vị trí cuối cùng của phần tử lớn nhaast :",vi_tri_max_cuoi)