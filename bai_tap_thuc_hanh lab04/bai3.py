x = float(input('Nhập X: '))
cos_x = 1
term = 1
N = 1
while abs(term) > 1e-4:
    N += 1
    term *= (-1) * x**2 / ((2*N - 1) * (2*N))
    cos_x += term
print('Cos(x) =', cos_x)