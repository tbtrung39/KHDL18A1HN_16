import math

def is_TamGiac(a, b, c):
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
        return False
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)

def ChuViTamGiac(a, b, c):
    if not is_TamGiac(a, b, c):
        return "Không phải là tam giác"
    return a + b + c

def DienTichTamGiac(a, b, c):
    if not is_TamGiac(a, b, c):
        return "Không phải là tam giác"
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == "__main__":
    print("Đây là module my_Triangle. Vui lòng chạy file chương trình chính để sử dụng.")