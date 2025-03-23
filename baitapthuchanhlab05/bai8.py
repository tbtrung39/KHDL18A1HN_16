chuoi_str = input("Nhập chuỗi Str: ")
tu_don = input("Nhập từ đơn cần tìm: ")
dem = 0
i = 0
while i < len(chuoi_str):
    j = 0
    while j < len(tu_don) and i + j < len(chuoi_str) and chuoi_str[i + j] == tu_don[j]:
        j += 1
    if j == len(tu_don):
        dem += 1
    i += 1
print("Số lần xuất hiện của từ", tu_don, "trong chuỗi Str là:", dem)