def hoan_vi(n):
    if n == 1 :
        return [[1]]
    else:
        ket_qua = []
        cac_hoan_vi_truoc = hoan_vi(n -1)
        for p in cac_hoan_vi_truoc:
            for i in range(len(p) + 1):
                hoan_vi_moi = p[:i] + [n] + p[i:]
                ket_qua.append(hoan_vi_moi)
        return ket_qua
    
n = int(input("Nhập số n:"))
ds_hoan_vi = hoan_vi(n)
print("Tất cả hoán vị từ dãy 1 đến ", n, "là:")
for hv in ds_hoan_vi:
    print(hv)