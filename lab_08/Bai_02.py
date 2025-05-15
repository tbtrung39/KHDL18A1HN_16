def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln = tim_ucln(tu, mau)
    tu_moi = tu // ucln
    mau_moi = mau // ucln
    return tu_moi, mau_moi

tu = int(input("Nhập tử số: "))
mau = int(input("Nhập mẫu số: "))

if mau == 0:
    print("Lỗi: Mẫu số không được bằng 0.")
else:
    tu_moi, mau_moi = rut_gon_phan_so(tu, mau)
    print(f"Phân số rút gọn: {tu_moi}/{mau_moi}")
