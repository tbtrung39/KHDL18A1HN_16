  
so = int(input("Nhập một số nguyên có 3 chữ số: "))
if (so >= 100 and so <= 999) or (so <= -100 and so >= -999):
    dau = ""
    if so < 0:
        dau = "Âm "
        so = -so  # Đổi sang dương để dễ tách chữ số

    # Tách từng chữ số hàng trăm, hàng chục, hàng đơn vị
    hang_tram = so // 100
    hang_chuc = (so // 10) % 10
    hang_dv   = so % 10

    # Danh sách đọc cơ bản
    so_doc = ["không", "một", "hai", "ba", "bốn", 
              "năm", "sáu", "bảy", "tám", "chín"]

    # Bắt đầu ghép cách đọc
    doc_so = dau  # nếu là số âm thì thêm "Âm"
    doc_so += so_doc[hang_tram] + " trăm"

    # Xử lý hàng chục
    if hang_chuc == 0:
        if hang_dv != 0:
            doc_so += " lẻ"
    elif hang_chuc == 1:
        # Nếu hàng chục là 1, đọc "mười"
        doc_so += " mười"
    else:
        # Nếu hàng chục >= 2
        doc_so += " " + so_doc[hang_chuc] + " mươi"

    # Xử lý hàng đơn vị
    if hang_chuc == 0:
        # Trường hợp hàng chục = 0, nếu hàng đơn vị != 0 thì đọc luôn
        if hang_dv != 0:
            doc_so += " " + so_doc[hang_dv]
    elif hang_chuc == 1:
        # Nếu hàng chục = 1
        if hang_dv == 5:
            doc_so += " lăm"  # mười lăm
        elif hang_dv != 0:
            doc_so += " " + so_doc[hang_dv]
    else:
        # Nếu hàng chục >= 2
        if hang_dv == 1:
            doc_so += " mốt"
        elif hang_dv == 5:
            doc_so += " lăm"
        elif hang_dv != 0:
            doc_so += " " + so_doc[hang_dv]

    # In ra kết quả
    print("Cách đọc của số nguyên là:", doc_so)
else:
    print("Số không hợp lệ! Vui lòng nhập một số nguyên có đúng 3 chữ số.")