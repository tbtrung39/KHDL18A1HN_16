danh_sach_sinh_vien = []
so_sinh_vien = int(input("Nhập số lượng sinh viên: "))

for _ in range(so_sinh_vien):
    ma_sinh_vien = input("Nhập mã sinh viên (6 ký tự số): ")
    while len(ma_sinh_vien) != 6 or not ma_sinh_vien.isdigit():
        print("Mã sinh viên phải là 6 ký tự số.")
        ma_sinh_vien = input("Nhập mã sinh viên (6 ký tự số): ")
    ten_sinh_vien = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm sinh viên (0-10): "))
    while diem < 0 or diem > 10:
        print("Điểm phải nằm trong khoảng từ 0 đến 10.")
        diem = float(input("Nhập điểm sinh viên (0-10): "))
    diem = round(diem)
    sinh_vien = {
        "ma_sinh_vien": ma_sinh_vien,
        "ten_sinh_vien": ten_sinh_vien,
        "diem": diem
    }
    danh_sach_sinh_vien.append(sinh_vien)
danh_sach_sinh_vien = sorted(danh_sach_sinh_vien, key=lambda x: x["diem"], reverse=True)
print("\nDanh sách sinh viên đã sắp xếp theo điểm số:")
for sinh_vien in danh_sach_sinh_vien:
    print(f"Mã sinh viên: {sinh_vien['ma_sinh_vien']}, Tên: {sinh_vien['ten_sinh_vien']}, Điểm: {sinh_vien['diem']}")