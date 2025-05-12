# giai_pt.py

import math

def giai_pt_bac_nhat(a, b):
    if a == 0:
        if b == 0:
            return "Phương trình vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Nghiệm của phương trình là x = {x}"

def giai_pt_bac_hai(a, b, c):
    if a == 0:
        # Nếu a = 0, chuyển về phương trình bậc nhất bx + c = 0
        return giai_pt_bac_nhat(b, c)

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm."
    elif delta == 0:
        x = -b / (2 * a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"