def sao_chep_tap_tin_voi_except():
    ten_tap_tin_nguon = input("Vui lòng nhập tên tập tin nguồn: ")
    ten_tap_tin_dich = input("Vui lòng nhập tên tập tin đích bạn muốn ghi: ")

    tap_tin_nguon = None
    tap_tin_dich = None

    try:
        tap_tin_nguon = open(ten_tap_tin_nguon, 'r')
        noi_dung = tap_tin_nguon.read()
        print(f"Đã đọc thành công nội dung từ '{ten_tap_tin_nguon}'.")

        try:
            tap_tin_dich = open(ten_tap_tin_dich, 'w')
            tap_tin_dich.write(noi_dung)
            print(f"Đã ghi thành công nội dung vào '{ten_tap_tin_dich}'.")
        except PermissionError:
            print(f"Lỗi: Không có quyền ghi vào tập tin '{ten_tap_tin_dich}'.")
        except Exception as e:
            print(f"Đã xảy ra lỗi khi mở hoặc ghi vào tập tin '{ten_tap_tin_dich}': {e}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy tập tin nguồn '{ten_tap_tin_nguon}'.")
    except PermissionError:
        print(f"Lỗi: Không có quyền đọc tập tin nguồn '{ten_tap_tin_nguon}'.")
    except Exception as e:
        print(f"Đã xảy ra lỗi khi mở hoặc đọc tập tin nguồn '{ten_tap_tin_nguon}': {e}")

    finally:
        if tap_tin_nguon:
            tap_tin_nguon.close()
            print(f"Đã đóng tập tin nguồn '{ten_tap_tin_nguon}'.")
        if tap_tin_dich:
            tap_tin_dich.close()
            print(f"Đã đóng tập tin đích '{ten_tap_tin_dich}'.")

if __name__ == "__main__":
    sao_chep_tap_tin_voi_except()