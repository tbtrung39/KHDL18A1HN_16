
sbd_to_phach = {}
with open("Bài_tập_thực_Hành/Sbd_Ph.dat", "r") as f:
    for line in f:
        sbd, phach = map(int, line.strip().split())
        sbd_to_phach[sbd] = phach

sbd_to_hoten = {}
with open("Bài_tập_thực_Hành/Sbd_Ten.txt", "r") as f:
    for line in f:
        parts = line.strip().split()
        sbd = int(parts[0])
        hoten = " ".join(parts[1:])
        sbd_to_hoten[sbd] = hoten

phach_to_diem = {}
with open("Bài_tập_thực_Hành/Phieu_Diem.txt", "r") as f:
    for line in f:
        phach, diem = map(int, line.strip().split())
        phach_to_diem[phach] = diem

ketqua = []
for sbd in sbd_to_phach:
    phach = sbd_to_phach[sbd]
    hoten = sbd_to_hoten.get(sbd, "Unknown")
    diem = phach_to_diem.get(phach, -1)  
    ketqua.append((sbd, hoten, diem))

ketqua.sort(key=lambda x: x[2], reverse=True)

with open("Bài_tập_thực_Hành/Ketqua.txt", "w") as f:
    for sbd, hoten, diem in ketqua:
        f.write(f"{sbd} {hoten} {diem}\n")