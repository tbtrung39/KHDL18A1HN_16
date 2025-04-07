
sinh_vien = {}

# Nhập thông tin cho 3 sinh viên (có thể thay số lượng bằng biến n tự đếm vòng lặp)
i = 0
while i < 3:
    print("Nhập thông tin sinh viên thứ", i + 1)
    ma_sv = input("Mã sinh viên (6 số): ")
    ho_ten = input("Họ và tên: ")
    diem = int(input("Điểm (0–10): "))
    sinh_vien[ma_sv] = {'ho_ten': ho_ten, 'diem': diem}
    i += 1

# Sắp xếp theo điểm giảm dần (không dùng sorted, chỉ dùng vòng lặp)
danh_sach = []

# Chuyển từ điển thành danh sách để sắp xếp
for key in sinh_vien:
    danh_sach.append((key, sinh_vien[key]['ho_ten'], sinh_vien[key]['diem']))

# Sắp xếp bubble sort theo điểm giảm dần
i = 0
while i < len(danh_sach) - 1:
    j = 0
    while j < len(danh_sach) - i - 1:
        if danh_sach[j][2] < danh_sach[j + 1][2]:
            tmp = danh_sach[j]
            danh_sach[j] = danh_sach[j + 1]
            danh_sach[j + 1] = tmp
        j += 1
    i += 1

# In kết quả
print("\nDanh sách sinh viên theo điểm giảm dần:")
for sv in danh_sach:
    print("Mã:", sv[0], "| Tên:", sv[1], "| Điểm:", sv[2])