import math
def giai_pt_bac_nhat(a, b):
    """
    Giải phương trình bậc nhất ax + b = 0
    """
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    return f"x = {-b/a}"
def giai_pt_bac_hai(a, b, c):
    """
    Giải phương trình bậc hai ax^2 + bx + c = 0
    """
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    
    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b/(2*a)
        return f"x1 = x2 = {x}"
    else:
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        return f"x1 = {x1}, x2 = {x2}"
if __name__ == "__main__":
    print("1. Giải phương trình bậc nhất ax + b = 0")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    print(giai_pt_bac_nhat(a, b))
    
    print("\n2. Giải phương trình bậc hai ax^2 + bx + c = 0")
    a = float(input("Nhập hệ số a: "))
    b = float(input("Nhập hệ số b: "))
    c = float(input("Nhập hệ số c: "))
    print(giai_pt_bac_hai(a, b, c))