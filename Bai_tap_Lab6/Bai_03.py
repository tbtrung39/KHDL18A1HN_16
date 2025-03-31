a = []
while True:
    num = int(input("Nhập số (0 để kết thúc): "))
    if num == 0:
        break
    a.append(num)
a_sorted = [x for x in a if x > 0] + [x for x in a if x <= 0]
print("Danh sách sau khi chuyển:", a_sorted)
m = int(input("Nhập số m: "))
a.insert(0, m)  
a.append(m)     
if len(a) >= 5:
    a.insert(4, m)  
else:
    a.append(m)  
print("Danh sách sau khi chèn:", a)