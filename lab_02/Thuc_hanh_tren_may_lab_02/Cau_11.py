# Nhập ngày và tháng
ngay = int(input("Nhập ngày: "))
thang = int(input("Nhập tháng: "))

# Xác định số ngày trong tháng (năm không nhuận)
if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
    so_ngay_trong_thang = 31
elif thang == 4 or thang == 6 or thang == 9 or thang == 11:
    so_ngay_trong_thang = 30
elif thang == 2:
    so_ngay_trong_thang = 28
else:
    print("Tháng không hợp lệ!")
    so_ngay_trong_thang = 0  # Để tránh lỗi khi nhập tháng sai

# Kiểm tra ngày nhập có hợp lệ không
if ngay < 1 or ngay > so_ngay_trong_thang:
    print("Ngày không hợp lệ!")
else:
    # Xác định ngày tiếp theo
    if ngay < so_ngay_trong_thang:
        ngay_tiep_theo = ngay + 1
        thang_tiep_theo = thang
    else:  # Trường hợp ngày cuối cùng của tháng
        ngay_tiep_theo = 1
        if thang == 12:  # Nếu là 31/12 thì sang 1/1 năm sau
            thang_tiep_theo = 1
        else:
            thang_tiep_theo = thang + 1

    # Xuất kết quả
    print("Ngày tiếp theo là:", ngay_tiep_theo, "/", thang_tiep_theo)