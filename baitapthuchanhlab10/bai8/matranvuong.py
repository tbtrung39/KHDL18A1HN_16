def nhap_kich_thuoc():
    while True:
        try:
            n = int(input("Nhập kích thước N của ma trận vuông: "))
            if n > 0:
                return n
            else:
                print("Kích thước ma trận phải là số nguyên dương.")
        except ValueError:
            print("Lỗi: Vui lòng nhập một số nguyên.")

def nhap_ma_tran(n):
    ma_tran = []
    print("Nhập các phần tử của ma trận:")
    for i in range(n):
        row = []
        for j in range(n):
            while True:
                try:
                    phan_tu = float(input(f"Nhập phần tử tại vị trí [{i+1}][{j+1}]: "))
                    row.append(phan_tu)
                    break
                except ValueError:
                    print("Lỗi: Vui lòng nhập một số.")
        ma_tran.append(row)
    return ma_tran

def in_ma_tran(ma_tran):
    """In ma trận ra màn hình theo định dạng."""
    n = len(ma_tran)
    for i in range(n):
        print(" ".join(map(str, ma_tran[i])))

def chuyen_vi_ma_tran(ma_tran):
    """Tính ma trận chuyển vị của ma trận vuông."""
    n = len(ma_tran)
    ma_tran_chuyen_vi = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ma_tran_chuyen_vi[j][i] = ma_tran[i][j]
    return ma_tran_chuyen_vi

def la_ma_tran_doi_xung(ma_tran):
    """Kiểm tra xem ma trận có phải là ma trận đối xứng không."""
    n = len(ma_tran)
    for i in range(n):
        for j in range(i + 1, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True

if __name__ == "__main__":
    print("Đây là module Matranvuong. Vui lòng chạy file chương trình chính để sử dụng.")