sinh_vien = {}
n = int(input("Nhập số lượng sinh viên: "))

for i in range(n):
    print(f"\nNhập thông tin sinh viên thứ {i+1}:")
    ma_sv = input("Mã sinh viên (6 chữ số): ")
    while not (ma_sv.isdigit() and len(ma_sv) == 6):
        ma_sv = input("Mã không hợp lệ. Nhập lại (6 chữ số): ")

    ten = input("Tên sinh viên: ")

    diem = float(input("Nhập điểm: "))
    diem_lam_tron = round(diem)
    diem_lam_tron = max(0, min(diem_lam_tron, 10))
    sinh_vien[ma_sv] = (ten, diem_lam_tron)
sinh_vien_sap_xep = sorted(sinh_vien.items(), key=lambda x: x[1][1], reverse=True)
print("\nDanh sách sinh viên sắp xếp theo điểm giảm dần:")
print("{:<10} {:<20} {:<5}".format("Mã SV", "Tên", "Điểm"))
for ma, (ten, diem) in sinh_vien_sap_xep:
    print("{:<10} {:<20} {:<5}".format(ma, ten, diem))