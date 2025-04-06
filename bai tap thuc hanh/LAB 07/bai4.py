chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170, 174, 150, 142, 148, 165, 170, 178, 156, 145, 149,
            163, 162, 159, 165, 165, 170, 180, 155, 159, 155, 153, 152, 162, 180, 168, 169, 168, 167, 170]

# a. Số lượng sinh viên trong nhóm
so_luong = len(chieu_cao)
print("Số lượng sinh viên:", so_luong)

# b. Tính chiều cao trung bình
chieu_cao_tb = sum(chieu_cao) / so_luong
print("Chiều cao trung bình:", chieu_cao_tb)

# c. Liệt kê các chiều cao khác nhau
chieu_cao_khac_nhau = sorted(set(chieu_cao))
print("Các chiều cao khác nhau:", chieu_cao_khac_nhau)