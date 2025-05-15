
import csv
from ibs.xu_ly_ttnv import tinh_luong, tinh_phu_cap, tinh_thuc_linh, sap_xep_theo_thuc_linh

ds_nv = []

def nhap_nhan_vien():
    ma_nv = input("Nhập mã NV: ")
    ten_nv = input("Nhập tên NV: ")
    chuc_vu = input("Nhập chức vụ (TP/PP/NV): ")
    he_so_luong = float(input("Nhập hệ số lương: "))

    luong = tinh_luong(he_so_luong)
    phu_cap = tinh_phu_cap(chuc_vu)
    thuc_linh = tinh_thuc_linh(he_so_luong, chuc_vu)

    nv = {
        "ma_nv": ma_nv,
        "ten_nv": ten_nv,
        "chuc_vu": chuc_vu,
        "he_so_luong": he_so_luong,
        "luong": luong,
        "phu_cap": phu_cap,
        "thuc_linh": thuc_linh
    }
    ds_nv.append(nv)

def in_danh_sach(ds):
    print(f"{'Mã NV':<10}{'Tên NV':<20}{'Chức vụ':<10}{'HSL':<5}{'Lương':<10}{'Phụ cấp':<10}{'Thực lĩnh':<12}")
    for nv in ds:
        print(f"{nv['ma_nv']:<10}{nv['ten_nv']:<20}{nv['chuc_vu']:<10}{nv['he_so_luong']:<5}{nv['luong']:<10,.0f}{nv['phu_cap']:<10,.0f}{nv['thuc_linh']:<12,.0f}")

def luu_file_csv():
    with open("C:\\Users\\nguye\\OneDrive\\Documents\\KHDL18A1HN_16\\bài tập thực hành\\câu 8\\LAB11\\files", mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã NV", "Tên NV", "Chức vụ", "HSL", "Lương", "Phụ cấp", "Thực lĩnh"])
        for nv in ds_nv:
            writer.writerow([nv["ma_nv"], nv["ten_nv"], nv["chuc_vu"], nv["he_so_luong"],
                             nv["luong"], nv["phu_cap"], nv["thuc_linh"]])
    print("Đã lưu danh sách nhân viên vào files/ds_nhanvien.csv")