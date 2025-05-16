def sao_chep_tap_tin():
    try:
        ten_tap_tin = input("Nhập tên tập tin cần đọc: ").strip()
        with open(ten_tap_tin, 'r', encoding='utf-8') as f_in:
            noi_dung = f_in.read()

        with open('copy.dat', 'w', encoding='utf-8') as f_out:
            f_out.write(noi_dung)

        print("Đã sao chép nội dung vào 'copy.dat' thành công.")

    except FileNotFoundError:
        print("Lỗi: Không tìm thấy tập tin.")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

sao_chep_tap_tin()
