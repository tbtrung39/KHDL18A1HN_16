# Nhập danh sách các phần tử tự nhiên cho đến khi nhập số 0
lst = []
while True:
    num = int(input("Nhập một số tự nhiên (nhập 0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Yêu cầu 1: Chèn danh sách [1, 2, 3] vào đầu, cuối và thứ 5 của danh sách
insert_list = [1, 2, 3]

# Chèn vào đầu
lst = insert_list + lst

# Chèn vào cuối
lst = lst + insert_list

# Chèn vào vị trí thứ 5 nếu danh sách có ít nhất 5 phần tử
if len(lst) >= 5:
    lst = lst[:5] + insert_list + lst[5:]
else:
    print("Danh sách có ít hơn 5 phần tử, không thể chèn vào vị trí thứ 5.")

# In danh sách sau khi chèn
print("Danh sách sau khi chèn:", lst)

# Yêu cầu 2: Xóa phần tử thứ k
k = int(input("Nhập chỉ số k để xóa phần tử thứ k trong danh sách: "))
if k < len(lst):
    lst = lst[:k] + lst[k+1:]
else:
    print("Chỉ số k không hợp lệ.")

# In danh sách sau khi xóa
print("Danh sách sau khi xóa phần tử thứ k:", lst)

# Yêu cầu 3: Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
# Sắp xếp tăng dần
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Danh sách sau khi sắp xếp tăng dần:", lst)

# Sắp xếp giảm dần
for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] < lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Danh sách sau khi sắp xếp giảm dần:", lst)
