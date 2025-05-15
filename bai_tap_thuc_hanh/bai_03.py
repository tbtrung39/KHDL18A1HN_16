def doc_va_sao_chep_tt():
    ten_tt = input("nhập tên tập tin cần đọc: ")
    try:
        with open(ten_tt,'r',encoding = 'utf-8') as tap_tin_nguon:
            noidung = tap_tin_nguon.read()
            with open('coppy.dat','w',encoding='utf_8') as tap_tin_dich:
                tap_tin_dich.write(noidung)
                print("đã sao chép nội dung")
    except FileNotFoundError:
        print("lỗi,không tìm thấy tập tin", ten_tt)
    except Exception as loi:
        print("lôic xử lí tập tin", str(loi))
doc_va_sao_chep_tt()