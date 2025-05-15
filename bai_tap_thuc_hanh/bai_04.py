def xu_ly_tap_tin():
    ten_tap_tin_nguon = input("nhập tên tập tin nguồn: ")
    ten_tap_tin_dich = input("nhập tên tệp tin dịch: ")
    try:
        with open(ten_tap_tin_nguon, 'r', encoding='utf-8') as tap_tin_nguon:
            dlieu = tap_tin_nguon.read()
            try:
                with open(ten_tap_tin_dich, 'r', encoding='utf-8') as tap_tin_dich:
                    tap_tin_dich.write(dlieu)
                    print("đã sao chép vào", tap_tin_dich, "thành công")
            except PermissionError:
                print("lỗi:không có quyền vào thông tin dịch")
            except Exception as loi_ghi:
                print("lỗi ghi thông tin:", str(loi_ghi))
    except FileNotFoundError:
        print('lỗi,không tìm thấy tập tin')
    except PermissionError:
        print("lỗi,không có quyền vào thông tin nguồn")
    except Exception as loi_doc:
        print('lỗi khi đọc tập tin',str(loi_doc))
xu_ly_tap_tin()


           
            