def tim_nghiem(n, N, current=[], ket_qua=[]):
    if n == 1:
        ket_qua.append(current + [N])
    else:
        for i in range(N + 1):
            tim_nghiem(n - 1,N - i,current + [i],ket_qua)
    return ket_qua
N = int(input("Nhap tong N:"))
n = int(input("Nhap so luong bien n:"))
danh_sach_nghiem = tim_nghiem(n, N)
print(f"Tat ca cac bo nghiem (x1, x2, ...,x{n} thoa man tong bang {N}:")
for bo_nghiem in danh_sach_nghiem:
    print(bo_nghiem)