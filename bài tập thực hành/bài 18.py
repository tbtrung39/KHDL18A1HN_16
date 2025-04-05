# Tạo từ điển chứa thông tin thí sinh: {SBD: (Họ tên, Điểm)}
thisinh = {
    "123456": ("Nguyễn Thị Diệu Linh", 9.0),
    "234567": ("Phạm Quốc Việt", 9.5),
    "345678": ("Đào Thùy Dương", 8.9)
}
sbd = input("Nhập số báo danh cần tra cứu: ")

if sbd in thisinh:
   
    ho_ten, diem = thisinh[sbd]
    print(f"Tìm thấy thí sinh:")
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm thi: {diem}")
else:
    # Nếu không có, yêu cầu nhập và thêm vào từ điển
    print("Không tìm thấy thí sinh. Nhập thông tin mới:")
    ho_ten = input("Họ tên thí sinh: ")
    diem = float(input("Điểm thi: "))
    thisinh[sbd] = (ho_ten, diem)
    print("Đã thêm thí sinh mới vào hệ thống.")

# In toàn bộ danh sách sau cập nhật
print("\nDanh sách thí sinh hiện tại:")
for sbd, (ho_ten, diem) in thisinh.items():
    print(f"SBD: {sbd} | Họ tên: {ho_ten} | Điểm: {diem}")