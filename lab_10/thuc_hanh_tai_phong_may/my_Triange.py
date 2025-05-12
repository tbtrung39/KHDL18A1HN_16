import math

def is_TamGiac(a, b, c):
    # Điều kiện tồn tại tam giác: tổng 2 cạnh lớn hơn cạnh còn lại
    return a + b > c and a + c > b and b + c > a

def ChuViTamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        return a + b + c
    else:
        return None  # Không phải tam giác

def S_TamGiac(a, b, c):
    if is_TamGiac(a, b, c):
        p = (a + b + c) / 2  # Nửa chu vi
        # Công thức Heron tính diện tích
        return math.sqrt(p * (p - a) * (p - b) * (p - c))
    else:
        return None