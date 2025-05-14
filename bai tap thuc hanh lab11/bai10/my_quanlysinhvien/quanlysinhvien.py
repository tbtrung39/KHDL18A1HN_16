import csv

def tinh_diem_tl(diem_tb, diem_rl):
    return (diem_tb + diem_rl) / 2

def nhap_sinh_vien():
    ma_sv = input("Nhập mã SV: ")
    ho_ten = input("Nhập họ tên: ")
    diem_tb = float(input("Nhập điểm TB: "))
    diem_rl = float(input("Nhập điểm RL: "))
    diem_tl = tinh_diem_tl(diem_tb, diem_rl)

    return {
        "ma_sv": ma_sv,
        "ho_ten": ho_ten,
        "diem_tb": diem_tb,
        "diem_rl": diem_rl,
        "diem_tl": diem_tl
    }

def in_danh_sach(danh_sach):
    print(f"{'Mã SV':<10}{'Họ tên':<25}{'Điểm TB':<10}{'Điểm RL':<10}{'Điểm TL':<10}")
    for sv in danh_sach:
        print(f"{sv['ma_sv']:<10}{sv['ho_ten']:<25}{sv['diem_tb']:<10.2f}{sv['diem_rl']:<10.2f}{sv['diem_tl']:<10.2f}")

def luu_file_csv(danh_sach, file_path):
    with open(file_path, mode="w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach:
            writer.writerow([sv['ma_sv'], sv['ho_ten'], sv['diem_tb'], sv['diem_rl'], sv['diem_tl']])

def sap_xep_theo_diem_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv["diem_rl"])

def tim_sv_diem_tl_max(danh_sach):
    max_sv = max(danh_sach, key=lambda sv: sv["diem_tl"])
    return max_sv