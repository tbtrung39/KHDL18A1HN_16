def thong_tin_nv(ds):
    ds["Họ tên"] = input("Nhập họ tên: ")
    ds["Quê quán"] = input("Nhập quê quán: ")
    ds["Thâm niên"] = float(input("Nhập thâm niên: "))
    ds["Lương"] = tinh_lương(ds)
    return ds
def tinh_lương(ds):
    luong = float(input("Nhập lương: "))
    for _ in ds:
        luong = luong + (1 + 0.05 * ds["Thâm niên"])
    return luong
def xuat_thong_tin(ds):
    print(thong_tin_nv(ds))
ds = {}
xuat_thong_tin(ds)