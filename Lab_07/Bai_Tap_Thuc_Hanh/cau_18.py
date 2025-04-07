
thisinh = {
    "123456": ("Vũ Trần Duy Anh", 8.5),
    "234567": ("Bùi Quang Huy", 7.0),
    "345678": ("Vương Quốc Thái Bình", 9.2)
}
sbd = input("Nhập số báo danh cần tra cứu: ")

if sbd in thisinh:
   
    ho_ten, diem = thisinh[sbd]
    print(f"Tìm thấy thí sinh:")
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm thi: {diem}")
else:
   
    print("Không tìm thấy thí sinh. Nhập thông tin mới:")
    ho_ten = input("Họ tên thí sinh: ")
    diem = float(input("Điểm thi: "))
    thisinh[sbd] = (ho_ten, diem)
    print("Đã thêm thí sinh mới vào hệ thống.")

print("\nDanh sách thí sinh hiện tại:")
for sbd, (ho_ten, diem) in thisinh.items():
    print(f"SBD: {sbd} | Họ tên: {ho_ten} | Điểm: {diem}")