try:
    ten_file = input("Nhập tên file cần đọc: ")
    ten_ghi = input("Nhập tên file để ghi: ")
    with open(ten_file, 'r', encoding='utf-8') as f_in:
        content = f_in.read()
    with open(ten_ghi, 'w', encoding='utf-8') as f_out:
        f_out.write(content)
    print("Sao chép thành công.")
except FileNotFoundError:
    print("Lỗi: File không tồn tại.")
except IOError as e:
    print("Lỗi thao tác file:", e)