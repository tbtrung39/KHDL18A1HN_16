chieu_cao = [
    161, 182, 161, 154, 176, 170, 167, 171, 170, 174,
    150, 142, 148, 165, 170, 178, 156, 145, 149, 163,
    162, 159, 165, 165, 170, 180, 155, 159, 155, 153,
    152, 162, 180, 168, 169, 168, 167, 170
]
so_sv = len(chieu_cao)
print("a. Số lượng sinh viên:", so_sv)
tb = sum(chieu_cao) / so_sv
print("b. Chiều cao trung bình:", round(tb, 2))
chieu_cao_khac_nhau = set(chieu_cao)
print("c. Các chiều cao khác nhau:", sorted(chieu_cao_khac_nhau))
print("   Chiều cao trung bình:", round(tb, 2))