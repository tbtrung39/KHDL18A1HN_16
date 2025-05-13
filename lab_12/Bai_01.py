import math

def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    dien_tich = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return dien_tich

def la_tam_giac(a, b, c):
    return a + b > c and a + c > b and b + c > a

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    canh = [a, b, c]
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Các cạnh phải là số dương lớn hơn 0.")
    if not la_tam_giac(a, b, c):
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tạo thành tam giác.")

    dientich = tinh_dien_tich_tam_giac(a, b, c)
    print(f"Ba cạnh tam giác là: {canh}")
    print(f"Diện tích tam giác là: {dientich:.2f}")

except ValueError as ve:
    print("Lỗi giá trị:", ve)
except Exception as e:
    print("Đã xảy ra lỗi:", e)