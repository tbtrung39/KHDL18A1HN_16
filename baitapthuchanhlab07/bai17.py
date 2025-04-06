thong_tin_sinh_vien = {}
while True:
    ma_sv = input("Nhập Mã sinh viên (6 ký tự số, 'stop' để dừng): ")
    if ma_sv.lower() == 'stop':
        break
    if len(ma_sv) == 6 and ma_sv.isdigit():
        ten_sv = input("Nhập Tên sinh viên: ")
        diem_str = input("Nhập Điểm số (0-10): ")
        if diem_str.isdigit():
            diem = int(diem_str)
            if 0 <= diem <= 10:
                thong_tin_sinh_vien[ma_sv] = {'ten': ten_sv, 'diem': diem}
            else:
                print("Điểm số phải từ 0 đến 10.")
        else:
            print("Điểm số phải là số nguyên.")
    else:
        print("Mã sinh viên phải là 6 ký tự số.")

thong_ke_diem = {}
for ma_sv, info in thong_tin_sinh_vien.items():
    diem = info['diem']
    thong_ke_diem[diem] = thong_ke_diem.get(diem, []) + [(ma_sv, info['ten'])]

print("\nThống kê sinh viên theo điểm (giảm dần):")
for diem in range(10, -1, -1):
    if diem in thong_ke_diem:
        sinh_vien_cung_diem = thong_ke_diem[diem]
        for ma_sv, ten in sinh_vien_cung_diem:
            print(f"Điểm: {diem}, Mã SV: {ma_sv}, Tên: {ten}")