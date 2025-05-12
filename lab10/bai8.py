def nhap_ma_tran():
    """Nhập ma trận vuông"""
    n = int(input("Nhập kích thước ma trận N: "))
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Nhập hàng {i+1} (cách nhau bằng dấu cách): ").split()))
        matrix.append(row)
    return matrix
def in_ma_tran(matrix):
    """In ma trận"""
    for row in matrix:
        print(' '.join(map(str, row)))
def chuyen_vi(matrix):
    """Tính ma trận chuyển vị"""
    return [list(row) for row in zip(*matrix)]
def is_doi_xung(matrix):
    """Kiểm tra ma trận đối xứng"""
    return all(matrix[i][j] == matrix[j][i] for i in range(len(matrix)) for j in range(i))
if __name__ == "__main__":
    m = nhap_ma_tran()
    print("\nMa trận nhập vào:")
    in_ma_tran(m)
    
    print("\nMa trận chuyển vị:")
    in_ma_tran(chuyen_vi(m))
    
    print("\nMa trận đối xứng:" if is_doi_xung(m) else "\nMa trận không đối xứng")