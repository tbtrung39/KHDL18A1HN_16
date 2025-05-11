# Đọc file Sbd_Ph.dat: SBD -> Phách
with open("Thuc_hanh_tren_lop\cau5\sbd_ph.dat") as f:
    sbd_phach = dict(map(int, line.split()) for line in f)

# Đọc file Sbd_Ten.txt: SBD -> Họ tên
with open("Thuc_hanh_tren_lop\cau5\sbd_ten.txt") as f:
    sbd_ten = {int(line.split()[0]): " ".join(line.split()[1:]) for line in f}

# Đọc file Phieu_Diem.txt: Phách -> Điểm
with open("Thuc_hanh_tren_lop\cau5\phieu_diem.txt") as f:
    phach_diem = dict(map(int, line.split()) for line in f)

# Ghép dữ liệu: SBD, Họ tên, Điểm
ds = []
for sbd, phach in sbd_phach.items():
    if sbd in sbd_ten and phach in phach_diem:
        ds.append((sbd, sbd_ten[sbd], phach_diem[phach]))

# Sắp xếp theo điểm giảm dần
ds.sort(key=lambda x: -x[2])

# Ghi kết quả ra file Ketqua.txt
with open("Thuc_hanh_tren_lop\cau5\ketqua.txt", "w") as f:
    for sbd, ten, diem in ds:
        f.write(f"{sbd} {ten} {diem}\n")
