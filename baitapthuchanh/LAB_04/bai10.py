while True:
    N = int(input("Nhập số nguyên (nhập số âm để dừng): "))
    if N < 0:
        break
    so_tam = N
    ket_qua = ''
    while so_tam > 0:
        chu_so_dau = so_tam // (10 ** (len(str(so_tam)) - 1))
        so_tam = so_tam % (10 ** (len(str(so_tam)) - 1))
        if chu_so_dau == 0:
            ket_qua += "không "
        elif chu_so_dau == 1:
            ket_qua += "một "
        elif chu_so_dau == 2:
            ket_qua += "hai "
        elif chu_so_dau == 3:
            ket_qua += "ba "
        elif chu_so_dau == 4:
            ket_qua += "bốn "
        elif chu_so_dau == 5:
            ket_qua += "năm "
        elif chu_so_dau == 6:
            ket_qua += "sáu "
        elif chu_so_dau == 7:
            ket_qua += "bảy "
        elif chu_so_dau == 8:
            ket_qua += "tám "
        elif chu_so_dau == 9:
            ket_qua += "chín "

    print("Số", N, "dưới dạng chữ:", ket_qua.strip())