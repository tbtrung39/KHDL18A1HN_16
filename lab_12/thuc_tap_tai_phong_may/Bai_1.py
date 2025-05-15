import math

def tinh_dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

try:
    # Nhập dữ liệu
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    # Đưa vào danh sách
    sides = [a, b, c]

    # Kiểm tra số âm hoặc bằng 0
    if any(side <= 0 for side in sides):
        raise ValueError("Các cạnh tam giác phải là số dương lớn hơn 0.")

    # Kiểm tra điều kiện tồn tại tam giác
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tồn tại tam giác.")

    # Tính diện tích
    area = tinh_dien_tich_tam_giac(a, b, c)
    print(f"Ba cạnh tam giác là: {sides}")
    print(f"Diện tích tam giác là: {area:.2f}")

except ValueError as ve:
    print("Lỗi:", ve)
except Exception as e:
    print("Đã xảy ra lỗi không xác định:", e)