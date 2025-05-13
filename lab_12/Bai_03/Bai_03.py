try:
    path = input("Nhập đường dẫn đến file cần đọc: ")
    with open(r"lab_12\Bai_03\nd.txt", "r") as f:
        nd = f.read()
    with open("copy.dat", "w") as copy_f:
        copy_f.write(nd)
        print("Đã sao chép nội dung sang file 'copy.dat'")
except FileNotFoundError:
    print("Không tìm thấy file. Kết thúc chương trình.")
except OSError:
    print("Lỗi đường dẫn hoặc lỗi khi mở file.")