import os

def sao_chep_tap_tin():
    ten_tap_tin_nguoi_dung = input("Vui lòng nhập tên tập tin bạn muốn sao chép: ")

    if not os.path.exists(ten_tap_tin_nguoi_dung):
        print(f"Lỗi: Tập tin '{ten_tap_tin_nguoi_dung}' không tồn tại.")
        return

    try:
        with open(ten_tap_tin_nguoi_dung, 'r') as tap_tin_nguon:
            noi_dung = tap_tin_nguon.read()

        with open('copy.dat', 'w') as tap_tin_dich:
            tap_tin_dich.write(noi_dung)

        print(f"Đã sao chép thành công nội dung từ '{ten_tap_tin_nguoi_dung}' sang 'copy.dat'.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin '{ten_tap_tin_nguoi_dung}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi trong quá trình đọc hoặc ghi tập tin: {e}")

if __name__ == "__main__":
    sao_chep_tap_tin()