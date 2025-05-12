import csv

def nhap_sinh_vien():
    danh_sach = []
    n = int(input("Nhập số sinh viên: "))
    for _ in range(n):
        ma = input("Mã SV: ")
        hoten = input("Họ tên: ")
        diem_tb = float(input("Điểm TB: "))
        diem_rl = float(input("Điểm RL: "))
        diem_tl = (diem_tb + diem_rl) / 2
        sv = {
            "ma": ma,
            "hoten": hoten,
            "diem_tb": diem_tb,
            "diem_rl": diem_rl,
            "diem_tl": diem_tl
        }
        danh_sach.append(sv)
    return danh_sach

def ghi_file_csv(danh_sach, filename="files/ds_sinhvien.csv"):
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Mã SV", "Họ tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach:
            writer.writerow([sv["ma"], sv["hoten"], sv["diem_tb"], sv["diem_rl"], f"{sv['diem_tl']:.2f}"])

def in_danh_sach(danh_sach):
    print(f"{'Mã SV':<10}{'Họ tên':<20}{'TB':<6}{'RL':<6}{'TL':<6}")
    for sv in danh_sach:
        print(f"{sv['ma']:<10}{sv['hoten']:<20}{sv['diem_tb']:<6}{sv['diem_rl']:<6}{sv['diem_tl']:<6.2f}")

def sinh_vien_tl_cao_nhat(danh_sach):
    max_sv = danh_sach[0]
    for sv in danh_sach[1:]:
        if sv["diem_tl"] > max_sv["diem_tl"]:
            max_sv = sv
    return max_sv

def main():
    ds = nhap_sinh_vien()

    print("\nDanh sách sinh viên:")
    in_danh_sach(ds)

    ghi_file_csv(ds)

    print("\nSắp xếp danh sách theo điểm RL tăng dần:")
    ds.sort(key=lambda sv: sv["diem_rl"])
    in_danh_sach(ds)

    print("\nSinh viên có điểm TL cao nhất:")
    sv_max = sinh_vien_tl_cao_nhat(ds)
    print(f"{sv_max['ma']}, {sv_max['hoten']}, Điểm TL: {sv_max['diem_tl']:.2f}")

if __name__ == "__main__":
    main()
