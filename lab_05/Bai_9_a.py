from itertools import groupby

chuoi = input("Nhập chuỗi ký tự: ")

# Nhóm các ký tự liên tiếp giống nhau và tìm nhóm dài nhất
nhom_ky_tu = ["".join(nhom) for _, nhom in groupby(chuoi)]
do_dai_max = max(len(nhom) for nhom in nhom_ky_tu)  # Tìm độ dài lớn nhất
chuoi_max = [nhom for nhom in nhom_ky_tu if len(nhom) == do_dai_max]  # Lấy tất cả chuỗi dài nhất

print("Chuỗi con dài nhất:", ", ".join(chuoi_max))  # Hiển thị tất cả nếu có nhiều chuỗi cùng độ dài