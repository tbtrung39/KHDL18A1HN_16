def permutation(arr):
    if len(arr) == 1:
        return [arr]
    
    ket_qua = []
    for i in range(len(arr)):
        phan_tu = arr[i]
        con_lai = arr[:i] + arr[i+1:]
        for hoan_vi in permutation(con_lai):
            ket_qua.append([phan_tu] + hoan_vi)
    return ket_qua

n = int(input("Nhap n: "))
day = list(range(1, n + 1))
cac_hoan_vi = permutation(day)

for p in cac_hoan_vi:
    print(p)