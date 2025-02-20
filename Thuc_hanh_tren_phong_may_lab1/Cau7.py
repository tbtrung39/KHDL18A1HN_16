# 7

def tim_dinh_parabola(a, b, c):
    if a == 0:
        print("Đây không phải phương trình bậc 2.")
    else:
        x_dinh = -b / (2 * a)
        y_dinh = c - (b ** 2) / (4 * a)
        print(f"Đỉnh của parabol là: ({round(x_dinh, 2)}, {round(y_dinh, 2)})")

# Nhập dữ liệu từ bàn phím
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Gọi hàm mà không cần return
tim_dinh_parabola(a, b, c)