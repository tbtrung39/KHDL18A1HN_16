def nhap_phan_so():
    tu = int(input("Nhập tử số: "))
    mau = int(input("Nhập mẫu số: "))
    return tu, mau

def tim_ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def rut_gon_phan_so(tu, mau):
    ucln = tim_ucln(tu, mau)
    tu_moi = tu // ucln
    mau_moi = mau // ucln
    return tu_moi, mau_moi

def hien_thi_phan_so(tu, mau):
    print(f"Phân số rút gọn là: {tu}/{mau}")

# Chương trình chính
tu, mau = nhap_phan_so()
tu_gon, mau_gon = rut_gon_phan_so(tu, mau)
hien_thi_phan_so(tu_gon, mau_gon)