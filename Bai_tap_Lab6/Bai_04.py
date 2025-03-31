a = []
while True:
    num = int(input("Nhập số (0 để kết thúc): "))
    if num == 0:
        break
    a.append(num)
sub_list = [1, 2, 3]
a = sub_list + a  
a.extend(sub_list)  
if len(a) >= 5:
    a[4:4] = sub_list  
else:
    a.extend(sub_list)  
print("Danh sách sau khi chèn:", a)
k = int(input("Nhập vị trí k cần xóa: "))
if 0 < k <= len(a):
    del a[k-1]  
    print("Danh sách sau khi xóa:", a)
else:
    print("Vị trí không hợp lệ")
a_sorted_asc = sorted(a)  
a_sorted_desc = sorted(a, reverse=True)  
print("Danh sách tăng dần:", a_sorted_asc)
print("Danh sách giảm dần:", a_sorted_desc)