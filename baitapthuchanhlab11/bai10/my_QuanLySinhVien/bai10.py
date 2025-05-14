import os
def nhap_sinh_vien():
    """Nhập thông tin một sinh viên từ bàn phím."""
    ma_sv = input("Nhập Mã SV: ")
    ho_ten = input("Nhập Họ tên: ")
    diem_tb = float(input("Nhập Điểm TB: "))
    diem_rl = int(input("Nhập Điểm RL: "))
    return {"ma_sv": ma_sv, "ho_ten": ho_ten, "diem_tb": diem_tb, "diem_rl": diem_rl}

def tinh_diem_tl(sinh_vien):
    """Tính điểm tích lũy cho sinh viên."""
    sinh_vien["diem_tl"] = (sinh_vien["diem_tb"] + sinh_vien["diem_rl"]) / 2
    return sinh_vien

def hien_thi_danh_sach(danh_sach_sv):
    """Hiển thị danh sách sinh viên dưới dạng bảng."""
    print("-" * 60)
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'Điểm TB':<10}{'Điểm RL':<10}{'Điểm TL':<10}")
    print("-" * 60)
    for sv in danh_sach_sv:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<20}{sv['diem_tb']:<10.2f}{sv['diem_rl']:<10}{sv.get('diem_tl', 0):<10.2f}")
    print("-" * 60)

def luu_danh_sach(danh_sach_sv, ten_tep):
    """Lưu danh sách sinh viên vào tệp CSV."""
    thu_muc_files = "files"
    os.makedirs(thu_muc_files, exist_ok=True)
    duong_dan_tep = os.path.join(thu_muc_files, ten_tep)
    with open(duong_dan_tep, 'w', encoding='utf-8') as f:
        f.write("Mã SV,Họ tên,Điểm TB,Điểm RL,Điểm TL\n")
        for sv in danh_sach_sv:
            f.write(f"{sv['ma_sv']},{sv['ho_ten']},{sv['diem_tb']},{sv['diem_rl']},{sv.get('diem_tl', 0)}\n")
    print(f"Đã lưu danh sách sinh viên vào '{duong_dan_tep}'")

def sap_xep_theo_diem_rl(danh_sach_sv):
    """Sắp xếp danh sách sinh viên theo điểm RL tăng dần."""
    return sorted(danh_sach_sv, key=lambda sv: sv['diem_rl'])

def main():
    danh_sach_sinh_vien = []
    so_luong = int(input("Nhập số lượng sinh viên: "))
    print("--- Nhập thông tin sinh viên ---")
    for _ in range(so_luong):
        sv = nhap_sinh_vien()
        sv = tinh_diem_tl(sv)
        danh_sach_sinh_vien.append(sv)
    print("--- Hoàn tất nhập liệu ---")

    hien_thi_danh_sach(danh_sach_sinh_vien)
    luu_danh_sach(danh_sach_sinh_vien, "ds_sinhvien.csv")

    danh_sach_da_sap_xep = sap_xep_theo_diem_rl(danh_sach_sinh_vien)
    print("\n--- Danh sách sinh viên sau khi sắp xếp theo Điểm RL tăng dần ---")
    hien_thi_danh_sach(danh_sach_da_sap_xep)

if __name__ == "__main__":
    main()