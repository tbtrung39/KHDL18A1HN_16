def tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Các cạnh phải là số dương!")

    if not tam_giac(a, b, c):
        raise ValueError("Ba cạnh không tạo thành tam giác hợp lệ!")

    print(f"Ba cạnh ({a}, {b}, {c}) tạo thành một tam giác hợp lệ.")

except ValueError as e:
    print("Lỗi:", e)
except Exception:
    print("Lỗi: Dữ liệu nhập không hợp lệ!")