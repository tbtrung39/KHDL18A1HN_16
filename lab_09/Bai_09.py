def dao_nguoc_so(n, rev = 0):
    if n == 0:
        return rev
    else:
        chu_so_cuoi = n % 10
        rev = rev * 10 + chu_so_cuoi
        return dao_nguoc_so(n // 10, rev)
so = int(input("Nhập số: "))
ket_qua = dao_nguoc_so(so)
print("Số sau khi đảo ngược là :",ket_qua)
