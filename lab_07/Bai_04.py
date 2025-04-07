
chieu_cao = [161, 182, 161, 154, 176, 170, 167, 171, 170,\
             174, 150, 142, 148, 165, 170, 178, 156, 145, 149, 163, 162,\
             159, 165,170, 180, 155, 153, 152, 162, 180, 168, 169, 168, 167, 178]
so_luong_sinh_vien = len(chieu_cao)
chieu_cao_tb = sum(chieu_cao) / so_luong_sinh_vien
chieu_cao_khac_nhau = set(chieu_cao)
print("So luong sinh vien trong nhom:", so_luong_sinh_vien)
print("Chieu cao TB cua cac sinh vien:", round(chieu_cao_tb, 2))
print("Cac chieu cao khac nhau trong nhom:", sorted(chieu_cao_khac_nhau))
