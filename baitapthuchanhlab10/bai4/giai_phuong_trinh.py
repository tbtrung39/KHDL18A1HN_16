import math

def giai_phuong_trinh_bac_nhat(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Lỗi: Hệ số a và b phải là số."
    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm."
        else:
            return "Phương trình vô nghiệm."
    else:
        x = -b / a
        return f"Nghiệm của phương trình là x = {x}"

def giai_phuong_trinh_bac_hai(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        return "Lỗi: Các hệ số a, b, c phải là số."
    if a == 0:
        return giai_phuong_trinh_bac_nhat(b, c) 

    delta = b**2 - 4*a*c
    if delta < 0:
        return "Phương trình vô nghiệm thực."
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép x = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm thực phân biệt: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    print("Đây là module giai_phuong_trinh. Vui lòng chạy file chương trình chính để sử dụng.")