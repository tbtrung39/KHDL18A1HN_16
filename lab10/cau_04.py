def giai_pt_bac_nhat(a, b):
    """Giải phương trình bậc nhất ax + b = 0"""
    if a == 0:
        if b == 0:
            return "Vô số nghiệm"
        else:
            return "Vô nghiệm"
    return -b / a

def giai_pt_bac_hai(a, b, c):
    """Giải phương trình bậc hai ax^2 + bx + c = 0"""
    if a == 0:
        return giai_pt_bac_nhat(b, c)
    
    delta = b**2 - 4 * a * c

    if delta < 0:
        return "Vô nghiệm"
    elif delta == 0:
        x = -b / (2 * a)
        return f"Nghiệm kép: x = {x}"
    else:
        sqrt_delta = delta ** 0.5
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        return f"Hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"