def nhap_ma_tran(n):
    print(f"Nhập ma trận {n}x{n} (nhập từng dòng, cách nhau bởi dấu cách):")
    matran = []
    for i in range(n):
        while True:
            try:
                dong = list(map(int, input(f"Dòng {i + 1}: ").strip().split()))
                if len(dong) != n:
                    print(f"Vui lòng nhập đúng {n} phần tử.")
                else:
                    matran.append(dong)
                    break
            except ValueError:
                print("Vui lòng nhập các số nguyên.")
    return matran

def in_ma_tran(matran):
    print("Ma trận:")
    for dong in matran:
        print(" ".join(map(str, dong)))

def chuyen_vi(matran):
    n = len(matran)
    return [[matran[j][i] for j in range(n)] for i in range(n)]

def kiem_tra_doi_xung(matran):
    n = len(matran)
    for i in range(n):
        for j in range(i + 1, n):
            if matran[i][j] != matran[j][i]:
                return False
    return True