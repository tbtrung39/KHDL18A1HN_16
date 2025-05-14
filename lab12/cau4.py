
try:
    ten_vao = input("Nhập tên tập tin cần đọc: ")
    ten_ra = input("Nhập tên tập tin để ghi: ")

    with open(ten_vao, 'r', encoding='utf-8') as f_in:
        du_lieu = f_in.read()

    with open(ten_ra, 'w', encoding='utf-8') as f_out:
        f_out.write(du_lieu)

    print("Đã ghi nội dung từ", ten_vao, "sang", ten_ra)

except FileNotFoundError:
    print("Lỗi: Tập tin không tồn tại!")
except IOError:
    print("Lỗi: Không thể đọc hoặc ghi tập tin!")
