def nhap_ma_tran(n):
    print(f"Nhap ma tran {n}x{n}:")
    matran = []
    for i in range(n):
        row = []
        for j in range(n):
            val = float(input(f"Nhap phan tu [{i+1}][{j+1}]: "))
            row.append(val)
        matran.append(row)
    return matran

def in_ma_tran(m):
    print("Ma tran:")
    for row in m:
        for val in row:
            print(f"{val:.2f}", end="\t")
        print()

def chuyen_vi(m):
    n = len(m)
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(m[j][i])
        result.append(row)
    return result

def kiem_tra_doi_xung(m):
    n = len(m)
    for i in range(n):
        for j in range(n):
            if m[i][j] != m[j][i]:
                return False
    return True
