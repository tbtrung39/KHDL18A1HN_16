so_nguyen = int(input("Nhập một số nguyên có ba chữ số: "))

if 100 <= abs(so_nguyen) <= 999:
    hang_tram = abs(so_nguyen) // 100
    hang_chuc = (abs(so_nguyen) // 10) % 10
    hang_dv = abs(so_nguyen) % 10

    so_chu = ["không", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    ket_qua = so_chu[hang_tram] + " trăm"
    
    if hang_chuc == 0 and hang_dv != 0:
        ket_qua += " lẻ " + so_chu[hang_dv]
    elif hang_chuc == 1:
        ket_qua += " mười " + so_chu[hang_dv]
    elif hang_chuc > 1:
        ket_qua += " " + so_chu[hang_chuc] + " mươi"
        if hang_dv == 1:
            ket_qua += " mốt"
        elif hang_dv != 0:
            ket_qua += " " + so_chu[hang_dv]
    
    if so_nguyen < 0:
        ket_qua = "Âm " + ket_qua
    
    print("Cách đọc số là:", ket_qua)
else:
    print("Số nhập vào không phải số có ba chữ số!")