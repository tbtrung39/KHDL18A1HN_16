so_thu_nhat = int(input("Nhập số nguyên thứ nhất: "))
so_thu_hai = int(input("Nhập số nguyên thứ hai: "))

a = so_thu_nhat
b = so_thu_hai

ban_dau_1 = so_thu_nhat
ban_dau_2 = so_thu_hai

while b != 0:
    a, b = b, a % b

ucln = a
bcnn = (ban_dau_1 * ban_dau_2) // ucln

print("BCNN của", ban_dau_1, "và", ban_dau_2, "là:", bcnn)