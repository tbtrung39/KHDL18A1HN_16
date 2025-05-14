# Đọc dữ liệu từ các tập tin
with open("Sbd_Ph.dat", "r") as f:
    sbd_ph = dict(map(int, line.split()) for line in f)

with open("Sbd_Ten.txt", "r") as f:
    sbd_ten = {int(line.split()[0]): " ".join(line.split()[1:]) for line in f}

with open("Phieu_Diem.txt", "r") as f:
    ph_diem = dict(map(int, line.split()) for line in f)

# Ghép dữ liệu: sbd -> tên, điểm
result = []
for sbd, phach in sbd_ph.items():
    name = sbd_ten.get(sbd, "")
    diem = ph_diem.get(phach, 0)
    result.append((diem, sbd, name))

# Sắp xếp theo điểm giảm dần
result.sort(reverse=True)

# Ghi ra file
with open("Ketqua.txt", "w") as f:
    for diem, sbd, name in result:
        f.write(f"{sbd} {name} {diem}\n")
