# Nhập danh sách các phần tử số tự nhiên cho đến khi nhập vào số 0
lst = []
while True:
    num = int(input("Nhập một số tự nhiên (hoặc 0 để kết thúc): "))
    if num == 0:
        break
    lst.append(num)

# 1. Chèn danh sách [1, 2, 3] vào đầu, cuối và vị trí thứ 5 của danh sách
insert_list = [1, 2, 3]
lst = insert_list + lst  # Chèn vào đầu
lst.append(insert_list)  # Chèn vào cuối
if len(lst) >= 5:
    lst.insert(5, insert_list)  # Chèn vào vị trí thứ 5
else:
    lst.append(insert_list)  # Nếu ít hơn 5 phần tử, chèn vào cuối

print(f"Danh sách sau khi chèn: {lst}")

# 2. Xóa phần tử thứ k trong danh sách
k = int(input("Nhập chỉ số k của phần tử muốn xóa: "))
if 0 <= k < len(lst):
    del lst[k]
else:
    print("Chỉ số k không hợp lệ!")

print(f"Danh sách sau khi xóa phần tử thứ {k}: {lst}")

# 3. Sắp xếp danh sách theo thứ tự tăng dần và giảm dần
lst_sorted_asc = sorted(lst)
lst_sorted_desc = sorted(lst, reverse=True)

print(f"Danh sách sắp xếp tăng dần: {lst_sorted_asc}")
print(f"Danh sách sắp xếp giảm dần: {lst_sorted_desc}")
