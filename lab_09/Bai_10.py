def tinh_X(n, luu_ket_qua={}):
    if n in luu_ket_qua:
        return luu_ket_qua[n]

    if n == 0:
        luu_ket_qua[0] = 1
        return 1

    tong = 0
    for i in range(1, n + 1):
        tong += i**2 * tinh_X(n - i, luu_ket_qua)

    luu_ket_qua[n] = tong
    return tong
n = int(input("Nhập số nguyên n: "))
print("Giá trị X_n là:", tinh_X(n))