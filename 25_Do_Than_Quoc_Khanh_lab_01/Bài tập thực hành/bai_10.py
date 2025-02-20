import math
x = float(input("Nhập giá trị x: "))
if x > 0 and x != 1:
    log2_x = math.log2(x)
    f_x = (log2_x / 2) + (1 / log2_x)
    print(f"Giá trị của f(x): {f_x:.2f}")
else:
    print("Giá trị x không hợp lệ. x phải > 0 và ≠ 1.")
