try:
    ten_file = input("Nhập tên file cần đọc: ")
    with open(ten_file, 'r', encoding='utf-8') as f:
        data = f.read()
    with open("copy.dat", 'w', encoding='utf-8') as f_copy:
        f_copy.write(data)
    print("Đã sao chép nội dung vào copy.dat.")
except FileNotFoundError:
    print("Lỗi: Không tìm thấy tập tin.")