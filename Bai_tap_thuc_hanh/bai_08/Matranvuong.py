def nhap_ma_tran(n):
    ma_tran = []
    for i in range(n):
        dong = list(map(int, input(f"Nhập dòng {i+1}, cách nhau bằng dấu cách: ").split()))
        while len(dong) != n:
            print(f"Bạn phải nhập đúng {n} phần tử.")
            dong = list(map(int, input(f"Nhập lại dòng {i+1}: ").split()))
        ma_tran.append(dong)
    return ma_tran

def in_ma_tran(ma_tran):
    print("Ma trận:")
    for dong in ma_tran:
        print(" ".join(map(str, dong)))

def chuyen_vi(ma_tran):
    n = len(ma_tran)
    return [[ma_tran[j][i] for j in range(n)] for i in range(n)]

def kiem_tra_doi_xung(ma_tran):
    n = len(ma_tran)
    for i in range(n):
        for j in range(n):
            if ma_tran[i][j] != ma_tran[j][i]:
                return False
    return True
