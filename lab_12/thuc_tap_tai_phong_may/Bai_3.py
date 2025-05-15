def doc_va_sao_chep_file():
    try:
        # Nhập tên file từ bàn phím
        ten_file = input("Nhập tên file cần đọc: ")

        # Mở file ở chế độ đọc
        with open(ten_file, 'r', encoding='utf-8') as f:
            noi_dung = f.read()

        # Ghi nội dung vào file copy.dat
        with open('copy.dat', 'w', encoding='utf-8') as f_copy:
            f_copy.write(noi_dung)

        print("Đã sao chép nội dung thành công vào file 'copy.dat'")

    except FileNotFoundError:
        print("Lỗi: Tập tin không tồn tại")
    except Exception as e:
        print("Đã xảy ra lỗi:", e)

# Gọi hàm
doc_va_sao_chep_file()