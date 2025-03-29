# Nhập danh sách các số tự nhiên cho đến khi nhập vào số 0
lst = []
while True:
    num = int(input("Nhập số: "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

# Chèn danh sách
lst = [1, 2, 3] + lst + [1, 2, 3]
if len(lst) >= 5:
    lst = lst[:5] + [1, 2, 3] + lst[5:]

print("Danh sách sau khi chèn:", lst)

# Xóa phần tử thứ k 
k = int(input("Nhập vị trí cần xóa (1-based index): ")) - 1
if 0 <= k < len(lst):
    value_to_remove = lst[k]
    lst.remove(value_to_remove)  
else:
    print("Vị trí không hợp lệ!")

print("Danh sách sau khi xóa:", lst)

# Sắp xếp danh sách 
lst_tang = lst[:]
for i in range(len(lst_tang) - 1):
    for j in range(i + 1, len(lst_tang)):
        if lst_tang[i] > lst_tang[j]:
            lst_tang[i], lst_tang[j] = lst_tang[j], lst_tang[i]

lst_giam = lst[:]
for i in range(len(lst_giam) - 1):
    for j in range(i + 1, len(lst_giam)):
        if lst_giam[i] < lst_giam[j]:
            lst_giam[i], lst_giam[j] = lst_giam[j], lst_giam[i]

print("Danh sách sắp xếp tăng dần:", lst_tang)
print("Danh sách sắp xếp giảm dần:", lst_giam)
