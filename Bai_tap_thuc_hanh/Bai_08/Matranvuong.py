
def nhap_ma_tran(n):
    matran = []
    for i in range(n):
        hang = list(map(int, input(f"Nhập dòng {i+1}: ").split()))
        matran.append(hang)
    return matran

def in_ma_tran(matran):
    for row in matran:
        print(" ".join(map(str, row)))

def chuyen_vi(matran):
    return [list(row) for row in zip(*matran)]

def kiem_tra_doi_xung(matran):
    return matran == chuyen_vi(matran)
