from libs import QuanLySinhVien


def main():
    qlsv = QuanLySinhVien()
    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
        print("1. Nhập danh sách sinh viên")
        print("2. In danh sách sinh viên và lưu file CSV")
        print("3. Sắp xếp theo điểm rèn luyện")
        print("4. In sinh viên có điểm TL cao nhất")
        print("0. Thoát")

        chon = input("Chọn chức năng: ")
        if chon == '1':
            qlsv.nhap_sinh_vien()
        elif chon == '2':
            qlsv.xuat_danh_sach()
        elif chon == '3':
            qlsv.sap_xep_theo_rl()
            print("Đã sắp xếp danh sách theo điểm RL.")
        elif chon == '4':
            qlsv.in_sv_tl_max()
        elif chon == '0':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()