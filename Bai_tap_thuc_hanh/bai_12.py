
def tinh_luong(tham_nien):
    return 1_500_000 + tham_nien * 120_000

def xuat_nv(ho_ten, que_quan, tham_nien, luong):
    print("=== Thông tin nhân viên ===")
    print(f"Họ tên: {ho_ten}")
    print(f"Quê quán: {que_quan}")
    print(f"Thâm niên công tác: {tham_nien} năm")
    print(f"Lương: {luong:,} VND")

def nhap_va_xuat_nv():
    ho_ten = input("Nhập họ tên nhân viên: ")
    que_quan = input("Nhập quê quán: ")
    tham_nien = int(input("Nhập thâm niên công tác (năm): "))
    luong = tinh_luong(tham_nien)
    xuat_nv(ho_ten, que_quan, tham_nien, luong)

nhap_va_xuat_nv()
