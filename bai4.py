# Bài 4: Thống kê chiều cao sinh viên

ds = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170,
      178, 156, 145, 149, 163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
      152, 160, 182, 160, 168, 160, 167, 170]

# a. Đếm số sinh viên
so_sinh_vien = 0
for _ in ds:
    so_sinh_vien += 1
print("Số sinh viên trong nhóm:", so_sinh_vien)

# b. Tính chiều cao trung bình
tong = 0
dem = 0
for chieu_cao in ds:
    tong += chieu_cao
    dem += 1
trung_binh = tong / dem
print("Chiều cao trung bình:", trung_binh)

# c. Dùng set để lấy các chiều cao không trùng
tap_hop = set()
for chieu_cao in ds:
    tap_hop.add(chieu_cao)
print("Chiều cao không trùng:", tap_hop)

# d. Dùng dictionary đếm tần suất
tan_suat = {}
for chieu_cao in ds:
    if chieu_cao in tan_suat:
        tan_suat[chieu_cao] += 1
    else:
        tan_suat[chieu_cao] = 1

print("Tần suất chiều cao:")
for chieu_cao in tan_suat:
    print(f"{chieu_cao}: {tan_suat[chieu_cao]} lần")
