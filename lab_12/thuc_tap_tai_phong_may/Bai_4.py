def ghi_tep_van_ban():
    try:
        # Nhập tên file từ người dùng
        ten_file = input("Nhập tên file bạn muốn tạo/ghi (ví dụ: dulieu.txt): ")

        # Nhập nội dung từ bàn phím
        noi_dung = input("Nhập nội dung bạn muốn ghi vào file: ")

        # Mở file ở chế độ ghi (write mode)
        try:
            f = open(ten_file, 'r')  # cố tình mở sai chế độ để mô phỏng lỗi
            f.write(noi_dung)  # sẽ gây lỗi vì file mở ở chế độ 'r'
        except IOError:
            print("Lỗi: Mở file sai chế độ. Đang chuyển sang chế độ ghi 'w'...")

            # Mở lại ở chế độ ghi đúng
            f = open(ten_file, 'w', encoding='utf-8')
            f.write(noi_dung)
            print(f"Đã ghi nội dung vào tập tin '{ten_file}' thành công.")

    except Exception as e:
        print("Đã xảy ra lỗi:", e)
    finally:
        # Đảm bảo đóng file nếu nó đã được mở
        try:
            f.close()
            print("Đã đóng tập tin.")
        except:
            pass  # nếu f chưa được mở thì bỏ qua

# Gọi hàm
ghi_tep_van_ban()