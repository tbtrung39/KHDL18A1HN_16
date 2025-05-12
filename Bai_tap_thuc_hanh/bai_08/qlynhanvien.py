import csv
from libs.xu_ly_thong_tin_nhanvien import NhanVien

danh_sach_nv = []

def nhap_nhan_vien():
    n = int(input("Nhập số lượng nhân viên: "))
    for _ in range(n):
        ma = input("Mã NV: ")
        ten = input("Tên NV: ")
        chuc_vu = input("Chức vụ (TP/PP/NV): ")
        he_so_luong = input("Hệ số lương: ")
        nv = NhanVien(ma, ten, chuc_vu, he_so_luong)
        danh_sach_nv.append(nv)

def in_danh_sach():
    print(f"{'Mã':<10}{'Tên':<20}{'Chức vụ':<10}{'HSL':<5}{'Lương':<12}{'Phụ cấp':<10}{'Thực lĩnh':<12}")
    for nv in danh_sach_nv:
        print(f"{nv.ma:<10}{nv.ten:<20}{nv.chuc_vu:<10}{nv.he_so_luong:<5.2f}{nv.luong:<12,.0f}{nv.phu_cap:<10,.0f}{nv.thuc_linh:<12,.0f}")

def sap_xep_giam_thuc_linh():
    danh_sach_nv.sort(key=lambda x: x.thuc_linh, reverse=True)
    print("Đã sắp xếp theo Thực lĩnh giảm dần.")

def luu_file_csv():
    with open("files/ds_nhanvien.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã", "Tên", "Chức vụ", "Hệ số lương", "Lương", "Phụ cấp", "Thực lĩnh"])
        for nv in danh_sach_nv:
            writer.writerow([nv.ma, nv.ten, nv.chuc_vu, nv.he_so_luong, nv.luong, nv.phu_cap, nv.thuc_linh])
    print("Đã lưu vào ds_nhanvien.csv")

def menu():
    while True:
        print("\n1. Nhập danh sách nhân viên")
        print("2. In danh sách nhân viên")
        print("3. Sắp xếp theo thực lĩnh giảm dần")
        print("4. Lưu danh sách vào file")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")
        if chon == "1":
            nhap_nhan_vien()
        elif chon == "2":
            in_danh_sach()
        elif chon == "3":
            sap_xep_giam_thuc_linh()
        elif chon == "4":
            luu_file_csv()
        elif chon == "0":
            break
        else:
            print("Chức năng không hợp lệ.")

if __name__ == "__main__":
    menu()