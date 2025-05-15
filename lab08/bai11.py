def nhap_thong_tin(ds):
    ds["Họ và tên"] = str(input("Nhập họ và tên: "))
    ds["Điểm Toán"] = float(input("Nhập điểm toán: "))
    ds["Điểm Lý"] = float(input("Nhập điểm lý: "))
    ds["Điểm Hóa"] = float(input("Nhập điểm Hóa: "))
    return ds
def diem_tb(ds):
    for _ in ds:
        tong = (ds["Điểm Toán"] + ds["Điểm Lý"] + ds["Điểm Hóa"])/3
    return tong
def xuat(ds):
    print(nhap_thong_tin(ds))
    print(f"Điểm trung bình: {diem_tb(ds)}")
ds = {}
xuat(ds)