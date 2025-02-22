so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))

if 100 <= so_nguyen <= 999:
    hang_tram = so_nguyen // 100
    hang_chuc = (so_nguyen % 100) // 10
    hang_don_vi = so_nguyen % 10

    doc_hang_tram = {
        1: "một trăm",
        2: "hai trăm",
        3: "ba trăm",
        4: "bốn trăm",
        5: "năm trăm",
        6: "sáu trăm",
        7: "bảy trăm",
        8: "tám trăm",
        9: "chín trăm"
    }

    doc_hang_chuc = {
        0: "",
        1: "mười",
        2: "hai mươi",
        3: "ba mươi",
        4: "bốn mươi",
        5: "năm mươi",
        6: "sáu mươi",
        7: "bảy mươi",
        8: "tám mươi",
        9: "chín mươi"
    }

    doc_hang_don_vi = {
        0: "",
        1: "một",
        2: "hai",
        3: "ba",
        4: "bốn",
        5: "năm",
        6: "sáu",
        7: "bảy",
        8: "tám",
        9: "chín"
    }
    ket_qua = doc_hang_tram[hang_tram]

    if hang_chuc == 0 and hang_don_vi != 0:
      ket_qua += " lẻ " + doc_hang_don_vi[hang_don_vi]
    else:
      ket_qua += " " + doc_hang_chuc[hang_chuc] + " " + doc_hang_don_vi[hang_don_vi]

    print(ket_qua)
else:
    print("Số nhập vào không có ba chữ số.")