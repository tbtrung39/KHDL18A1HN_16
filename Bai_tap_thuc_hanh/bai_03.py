lst = []
while True:
    num = int(input("Nhập số (0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

# -
duong = []
am = []
for x in lst:
    if x > 0:
        duong.append(x)
    else:
        am.append(x)

lst = duong + am  
print("Danh sách sau khi chuyển số dương lên đầu:", lst)

# -
m = int(input("Nhập số m để chèn: "))

lst.insert(0, m)  
lst.append(m)  
if len(lst) >= 5:
    lst.insert(4, m)  

print("Danh sách sau khi chèn m:", lst)
