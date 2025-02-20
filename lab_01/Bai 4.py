x = float(input("Nhap x: "))
x_binh = x ** 2
x_mu_4 = x ** 4
can_bac_2 = (x_binh + 4) ** (1 / 2)
can_bac_7 = (x_mu_4 + 1) ** (1 / 7)
tu_so = -x + can_bac_2
mau_so = can_bac_7
f_x = tu_so / mau_so
print("Gia tri cua bieu thuc f(x) la:", round(f_x, 2))