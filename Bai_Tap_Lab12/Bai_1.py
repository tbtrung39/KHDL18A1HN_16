import math

def dien_tich_tam_giac(a, b, c):
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

try:
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Cạnh tam giác phải lớn hơn 0.")
    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Ba cạnh không thỏa mãn điều kiện tam giác.")
    
    dt = dien_tich_tam_giac(a, b, c)
    print(f"Diện tích tam giác là: {dt:.2f}")

except ValueError as e:
    print("Lỗi:", e)
except Exception as e:
    print("Lỗi không xác định:", e)