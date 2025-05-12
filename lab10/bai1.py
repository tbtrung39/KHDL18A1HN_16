import math
def is_TamGiac(a, b, c):
    """
    Kiểm tra xem 3 số a, b, c có tạo thành tam giác không
    """
    return a + b > c and a + c > b and b + c > a
def ChuviTamGiac(a, b, c):
    """
    Tính chu vi tam giác
    """
    if not is_TamGiac(a, b, c):
        return "Không phải tam giác"
    return a + b + c
def S_TamGiac(a, b, c):
    """
    Tính diện tích tam giác bằng công thức Heron
    """
    if not is_TamGiac(a, b, c):
        return "Không phải tam giác"
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))
if __name__ == "__main__":
    a = float(input("Nhập cạnh a: "))
    b = float(input("Nhập cạnh b: "))
    c = float(input("Nhập cạnh c: "))
    
    if is_TamGiac(a, b, c):
        print("Đây là tam giác")
        print(f"Chu vi: {ChuviTamGiac(a, b, c)}")
        print(f"Diện tích: {S_TamGiac(a, b, c)}")
    else:
        print("Đây không phải tam giác")