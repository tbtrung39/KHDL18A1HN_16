import os
from My_QuanLySinhvien import quanlysinhvien
danh_sach_sv = []

def menu():
    while True:
        print("\n--- MENU QUẢN LÝ SINH VIÊN ---")
        print("1. Nhập danh sách sinh viên")
        print("2. In danh sách sinh viên")
        print("3. Sắp xếp theo điểm RL tăng dần")
        print("4. Tìm sinh viên có điểm TL cao nhất")
        print("5. Lưu danh sách vào file")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")

        if chon == "1":
            so_sv = int(input("Nhập số lượng sinh viên: "))
            for _ in range(so_sv):
                sv = quanlysinhvien.nhap_sinh_vien()
                danh_sach_sv.append(sv)
        elif chon == "2":
            quanlysinhvien.in_danh_sach(danh_sach_sv)
        elif chon == "3":
            ds_sx = quanlysinhvien.sap_xep_theo_diem_rl(danh_sach_sv)
            quanlysinhvien.in_danh_sach(ds_sx)
        elif chon == "4":
            sv_max = quanlysinhvien.tim_sv_diem_tl_max(danh_sach_sv)
            print("\nSinh viên có điểm TL cao nhất:")
            quanlysinhvien.in_danh_sach([sv_max])
        elif chon == "5":
            os.makedirs("files", exist_ok=True)
            quanlysinhvien.luu_file_csv(danh_sach_sv, "files/ds_sinhvien.csv")
            print("Đã lưu danh sách vào file 'files/ds_sinhvien.csv'")
        elif chon == "0":
            break
        else:
            print("Chức năng không hợp lệ!")

if __name__ == "__main__":
    menu()