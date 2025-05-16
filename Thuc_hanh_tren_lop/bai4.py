def doc_va_ghi_tap_tin():
    try:
        ten_nguon = input("Nhập tên tập tin nguồn: ").strip()
        ten_dich = input("Nhập tên tập tin đích (do bạn đặt): ").strip()

        try:
            f_in = open(ten_nguon, 'r', encoding='utf-8')
        except Exception as e:
            print(f"Lỗi khi mở tập tin nguồn: {e}")
            return

        try:
            f_out = open(ten_dich, 'w', encoding='utf-8')
        except Exception as e:
            print(f"Lỗi khi mở tập tin đích: {e}")
            f_in.close()
            return

        noi_dung = f_in.read()
        f_out.write(noi_dung)
        print(f"Đã ghi nội dung vào tập tin '{ten_dich}' thành công.")

    except IOError as e:
        print(f"Lỗi I/O: {e}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")
    finally:
        # Đảm bảo đóng tệp nếu đã mở
        try:
            f_in.close()
        except:
            pass
        try:
            f_out.close()
        except:
            pass

doc_va_ghi_tap_tin()