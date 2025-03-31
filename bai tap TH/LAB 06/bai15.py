danh_sach = []
while True:
    nhap = input("Nhập (tên, tuổi, điểm) hoặc bấm Enter để dừng: ")
    if not nhap:
        break
    tach = nhap.split(",")
    if len(tach) == 3:
        ten = tach[0].strip()
        tuoi = int(tach[1].strip())
        diem = int(tach[2].strip())
        danh_sach.append((ten, tuoi, diem))
    else:
        print("Vui lòng nhập lạilại theo định dạng: tên, tuổi, điểm")

danh_sach_sap_xep = sorted(danh_sach, key=lambda x: (x[0], x[1], x[2]))

print("\nDanh sách đã sắp xếp:")
for muc in danh_sach_sap_xep:
    print(muc)