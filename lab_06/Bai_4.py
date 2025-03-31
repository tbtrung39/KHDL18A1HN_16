# Nhập danh sách số tự nhiên cho đến khi nhập 0
lst = []
while True:
    num = int(input("Nhập số (0 để dừng): "))
    if num == 0:
        break
    lst.append(num)

print("Danh sách ban đầu:", lst)

# Chèn danh sách [1,2,3] vào đầu, cuối và vị trí thứ 5
insert_list = [1, 2, 3]

# Chèn vào đầu danh sách
lst = insert_list + lst

# Chèn vào vị trí thứ 5 (nếu danh sách đủ dài)
if len(lst) >= 5:
    lst = lst[:5] + insert_list + lst[5:]
else:
    lst.extend(insert_list)  # Nếu không đủ 5 phần tử, chèn vào cuối

# Chèn vào cuối danh sách
lst.extend(insert_list)

print("Danh sách sau khi chèn:", lst)

# Xoá phần tử thứ k (k nhập từ bàn phím)
k = int(input("Nhập vị trí k cần xoá: "))
if 0 <= k < len(lst):
    del lst[k]
    print(f"Danh sách sau khi xoá phần tử thứ {k}:", lst)
else:
    print("Vị trí không hợp lệ!")

# Sắp xếp danh sách tăng dần
sorted_asc = sorted(lst)
print("Danh sách sắp xếp tăng dần:", sorted_asc)

# Sắp xếp danh sách giảm dần
sorted_desc = sorted(lst, reverse=True)
print("Danh sách sắp xếp giảm dần:", sorted_desc)