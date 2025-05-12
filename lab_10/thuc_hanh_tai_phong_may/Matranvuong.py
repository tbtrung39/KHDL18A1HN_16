# Matranvuong.py

def nhap_ma_tran(n):
    ma_tran = []
    print(f"Nhập ma trận {n}x{n}:")
    for i in range(n):
        dong = list(map(int, input(f"Dòng {i+1}: ").split()))
        while len(dong) != n:
            print("Sai số lượng phần tử. Nhập lại.")
            dong = list(map(int, input(f"Dòng {i+1}: ").split()))
        ma_tran.append(dong)
    return ma_tran

def in_ma_tran(m):
    for row in m:
        print(' '.join(map(str, row)))

def chuyen_vi(m):
    n = len(m)
    return [[m[j][i] for j in range(n)] for i in range(n)]

def kiem_tra_doi_xung(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True