chuoi = input("Nhập chuỗi ký tự: ")

do_dai_max = 0
chuoi_max_list = []
do_dai_hien_tai = 1  # Độ dài của chuỗi con đang xét

for i in range(1, len(chuoi)):
    if chuoi[i] == chuoi[i - 1]:  # Nếu ký tự giống ký tự trước đó
        do_dai_hien_tai += 1
    else:
        if do_dai_hien_tai > do_dai_max:  # Nếu tìm thấy chuỗi dài hơn
            do_dai_max = do_dai_hien_tai
            chuoi_max_list = [chuoi[i - 1] * do_dai_hien_tai]  # Cập nhật danh sách mới
        elif do_dai_hien_tai == do_dai_max:  # Nếu có cùng độ dài lớn nhất
            chuoi_max_list.append(chuoi[i - 1] * do_dai_hien_tai)
        do_dai_hien_tai = 1  # Reset độ dài cho ký tự mới

# Kiểm tra lần cuối sau khi vòng lặp kết thúc
if do_dai_hien_tai > do_dai_max:
    chuoi_max_list = [chuoi[-1] * do_dai_hien_tai]
elif do_dai_hien_tai == do_dai_max:
    chuoi_max_list.append(chuoi[-1] * do_dai_hien_tai)

print("Chuỗi con dài nhất:", ", ".join(chuoi_max_list))