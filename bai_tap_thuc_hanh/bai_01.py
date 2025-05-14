def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if is_triangle(a, b, c):
        print("Đây là một tam giác hợp lệ.")
    else:
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tam giác.")

except ValueError as e:
    print("Lỗi:", e)
except Exception:
    print("Lỗi: Vui lòng nhập đúng kiểu số.")