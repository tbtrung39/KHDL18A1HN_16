#Bước 1(Bài 8):
def nhap_ma_tran():
    n = int(input("Nhập kích thước ma trận N: "))
    ma_tran = []
    print("Nhập các phần tử của ma trận:")
    for i in range(n):
        dong = []
        for j in range(n):
            phan_tu = int(input(f"Phần tử [{i+1}][{j+1}]: "))
            dong.append(phan_tu)
        ma_tran.append(dong)
    return ma_tran

def in_ma_tran(ma_tran):
    n = len(ma_tran)
    for i in range(n):
        for j in range(n):
            print(ma_tran[i][j], end=" ")
        print()

def tinh_ma_tran_chuyen_vi(ma_tran):
    n = len(ma_tran)
    ma_tran_chuyen_vi = [[0 for _ in range(n)] for _ in range(n)] 
    for i in range(n):
        for j in range(n):
            ma_tran_chuyen_vi[j][i] = ma_tran[i][j]
    return ma_tran_chuyen_vi

def kiem_tra_doi_xung(ma_tran):
    n = len(ma_tran)
    for i in range(n):
        for j in range(n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True