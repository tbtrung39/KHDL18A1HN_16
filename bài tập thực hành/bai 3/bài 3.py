try:
    path = input("Nhập đường dẫn đến file cần đọc: ").strip()
    print("Đường dẫn đã nhập:", path)
    with open(path, "r", encoding="utf-8") as file:
        nd = file.read()
    with open("copy.dat", "w") as copy_f:
        copy_f.write(nd)
        print("Đã sao chép nội dung sang file 'copy.dat'")
except FileNotFoundError:
    print("Không tìm thấy file. Kết thúc chương trình.")
except OSError:
    print("Lỗi đường dẫn hoặc lỗi mở file.")
