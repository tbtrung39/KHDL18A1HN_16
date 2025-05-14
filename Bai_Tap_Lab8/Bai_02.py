import math
def rut_gon_phan_so(tu, mau):
    ucln = math.gcd(tu, mau)
    return tu // ucln, mau // ucln
tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))
if mau == 0:
    print("Phân số không hợp lệ (mẫu số bằng 0).")
else:
    tu_gon, mau_gon = rut_gon_phan_so(tu, mau)
    print(f"Phân số rút gọn là: {tu_gon}/{mau_gon}")