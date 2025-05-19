from My_quanlysinhvien import quanlysinhvien as qlsv

def main():
    danh_sach = qlsv.nhap_danh_sach_sv()
    
    print("\nDanh sách sinh viên:")
    qlsv.in_danh_sach_sv(danh_sach)

    qlsv.luu_vao_file(danh_sach)
    print("\nĐã lưu vào file dssinhvien.csv")

    danh_sach_sap_xep = qlsv.sap_xep_theo_diem_rl(danh_sach)
    print("\nDanh sách sau khi sắp xếp theo điểm RL:")
    qlsv.in_danh_sach_sv(danh_sach_sap_xep)

    sv_max = qlsv.tim_sv_diem_tl_cao_nhat(danh_sach)
    print("\nSinh viên có điểm TL cao nhất:")
    qlsv.in_danh_sach_sv([sv_max])

if __name__ == "__main__":
    main()