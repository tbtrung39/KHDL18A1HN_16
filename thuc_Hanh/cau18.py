diemthi = {
    "123": {"ten": "Nguyen Van A", "diem": 8.5},
    "124": {"ten": "Le Thi B", "diem": 9.0}
}
sbd = input("Nhập số báo danh: ")
if sbd in diemthi:
    print(diemthi[sbd])
else:
    print("Không tìm thấy.")
