x = float(input("Nhập giá trị x (rad): "))
result, term, n = 1.0, 1.0, 1
while abs(term) >= 1e-4:
    term *= -x**2 / ((2*n)*(2*n-1))
    result += term
    n += 1
print(f"Gần đúng giá trị cos({x}) là: {result}")
