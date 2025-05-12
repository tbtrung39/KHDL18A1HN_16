import csv
class SinhVien:
    def __init__(self, msv, hoten, diemTB, diemRL, diemTL=None):
        self.msv = msv
        self.hoten = hoten
        self.diemTB = float(diemTB)
        self.diemRL = float(diemRL)
        self.diemTL = diemTL
    def tinh_diem_tich_luy(self):
        self.diemTL = (self.diemTB * 0.8 + self.diemRL * 0.2)
        return self.diemTL
def nhap_danh_sach_sinh_vien():
    danh_sach = []
    while True:
        msv = input("Nhập mã sinh viên (hoặc 'done' để kết thúc): ")
        if msv.lower() == 'done':
            break
        hoten = input("Nhập họ tên sinh viên: ")
        while True:
            try:
                diemTB = float(input("Nhập điểm trung bình: "))
                if 0 <= diemTB <= 10:
                    break
                else:
                    print("Điểm trung bình phải từ 0 đến 10.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ cho điểm trung bình.")
        while True:
            try:
                diemRL = float(input("Nhập điểm rèn luyện: "))
                if 0 <= diemRL <= 100:
                    break
                else:
                    print("Điểm rèn luyện phải từ 0 đến 100.")
            except ValueError:
                print("Vui lòng nhập số hợp lệ cho điểm rèn luyện.")

        sinh_vien = SinhVien(msv, hoten, diemTB, diemRL)
        sinh_vien.tinh_diem_tich_luy()
        danh_sach.append(sinh_vien)
    return danh_sach
def in_danh_sach_sinh_vien(danh_sach, ten_file_csv="ds_sinhvien.csv"):
    print("\nDanh sách sinh viên:")
    print("{:<10} {:<20} {:<10} {:<10} {:<10}".format("Mã SV", "Họ Tên", "Điểm TB", "Điểm RL", "Điểm TL"))
    print("-" * 60)
    with open(ten_file_csv, 'w', newline='', encoding='utf-8') as file_csv:
        writer = csv.writer(file_csv)
        writer.writerow(["Mã SV", "Họ Tên", "Điểm TB", "Điểm RL", "Điểm TL"])
        for sv in danh_sach:
            print("{:<10} {:<20} {:<10.2f} {:<10.2f} {:<10.2f}".format(sv.msv, sv.hoten, sv.diemTB, sv.diemRL, sv.diemTL))
            writer.writerow([sv.msv, sv.hoten, f"{sv.diemTB:.2f}", f"{sv.diemRL:.2f}", f"{sv.diemTL:.2f}"])
    print(f"\nĐã lưu danh sách sinh viên vào file '{ten_file_csv}'")
def sap_xep_theo_diem_rl(danh_sach):
    return sorted(danh_sach, key=lambda sv: sv.diemRL)
def in_sinh_vien_diem_tl_cao_nhat(danh_sach):
    if not danh_sach:
        print("Danh sách sinh viên trống.")
        return
    sinh_vien_cao_nhat = max(danh_sach, key=lambda sv: sv.diemTL)
    print("\nSinh viên có điểm tích lũy cao nhất:")
    print("{:<10} {:<20} {:<10.2f} {:<10.2f} {:<10.2f}".format(
        sinh_vien_cao_nhat.msv, sinh_vien_cao_nhat.hoten, sinh_vien_cao_nhat.diemTB, sinh_vien_cao_nhat.diemRL, sinh_vien_cao_nhat.diemTL
    ))
if __name__ == "__main__":
    danh_sach_sinh_vien = nhap_danh_sach_sinh_vien()
    for sv in danh_sach_sinh_vien:
        sv.tinh_diem_tich_luy()
    in_danh_sach_sinh_vien(danh_sach_sinh_vien)
    danh_sach_da_sap_xep = sap_xep_theo_diem_rl(danh_sach_sinh_vien)
    print("\nDanh sách sinh viên sau khi sắp xếp theo điểm rèn luyện tăng dần:")
    in_danh_sach_sinh_vien(danh_sach_da_sap_xep, "ds_sinhvien_sapxep_rl.csv")
    in_sinh_vien_diem_tl_cao_nhat(danh_sach_sinh_vien)