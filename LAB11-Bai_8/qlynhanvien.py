import csv
from libs.xu_ly_thong_tin_nhanvien import tinh_luong, tinh_phu_cap, tinh_thuc_linh, sap_xep_theo_thuc_linh

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
    with open("LAB11-Bai_8/files/ds_nhanvien.csv", mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã NV", "Tên NV", "Chức vụ", "HSL", "Lương", "Phụ cấp", "Thực lĩnh"])
        for nv in ds_nv:
            writer.writerow([nv["ma_nv"], nv["ten_nv"], nv["chuc_vu"], nv["he_so_luong"],
                             nv["luong"], nv["phu_cap"], nv["thuc_linh"]])
    print("Đã lưu danh sách nhân viên vào files/ds_nhanvien.csv")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Nhập nhân viên")
        print("2. In danh sách nhân viên")
        print("3. Sắp xếp theo thực lĩnh giảm dần")
        print("4. Lưu vào file CSV")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            nhap_nhan_vien()
        elif chon == "2":
            in_danh_sach(ds_nv)
        elif chon == "3":
            ds_sx = sap_xep_theo_thuc_linh(ds_nv)
            in_danh_sach(ds_sx)
        elif chon == "4":
            luu_file_csv()
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    menu()