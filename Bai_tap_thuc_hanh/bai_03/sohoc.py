def Ucln(a, b):
    """Trả về ước chung lớn nhất của a và b"""
    while b != 0:
        a, b = b, a % b
    return a

def Bcnn(a, b):
    """Trả về bội chung nhỏ nhất của a và b"""
    return abs(a * b) // Ucln(a, b)
