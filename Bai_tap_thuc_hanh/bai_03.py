x = float(input("Nhập x (radian):"))
cos_x = 1
term = 1
n = 2
epsilon = 1e-4
while abs(term)>epsilon:
    term = (-term * x *x ) / ((n-1)*n)
    cos_x += term
    n += 2
print("giá trị xấp xỉ của cos(x):",cos_x)

