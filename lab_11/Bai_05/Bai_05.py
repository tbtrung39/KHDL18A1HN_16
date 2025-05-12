# Đọc file Sbd_Ph.dat
sbd_phach = {}
with open(r"lab_11\Bai_05\Sbd_Ph.dat", "r") as f:
    for line in f:
        if line.strip() == "":
            continue
        sbd, phach = line.strip().split()
        sbd_phach[phach] = sbd  # key: số phách, value: số báo danh

# Đọc file Sbd_Ten.txt
sbd_ten = {}
with open(r"lab_11\Bai_05\SBD_Ten.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        sbd = parts[0]
        ten = " ".join(parts[1:])
        sbd_ten[sbd] = ten

# Đọc file Phieu_Diem.txt và lắp ghép
ds_thi_sinh = []
with open(r"lab_11\Bai_05\Phieu_Diem.txt", "r") as f:
    for line in f:
        phach, diem = line.strip().split()
        if phach in sbd_phach:
            sbd = sbd_phach[phach]
            ten = sbd_ten.get(sbd, "Unknown")
            ds_thi_sinh.append((int(sbd), ten, float(diem)))

# Sắp xếp theo điểm giảm dần
ds_thi_sinh.sort(key=lambda x: x[2], reverse=True)

# Ghi ra file Ketqua.txt
with open("Ketqua.txt", "w") as f:
    for sbd, ten, diem in ds_thi_sinh:
        f.write(f"{sbd} {ten} {diem}\n")

print("Đã tạo file Ketqua.txt thành công.")