# Tạo từ điển chứa thông tin thí sinh
thisinh = {
    "A001": ["Nguyễn Văn An", 8.5],
    "A002": ["Trần Thị Bình", 7.75],
    "A003": ["Lê Văn Cường", 9.0]
}

# Nhập số báo danh cần tra cứu
sbd = input("Nhập số báo danh cần tra cứu: ")

# Kiểm tra sự tồn tại của số báo danh
if sbd in thisinh:
    print("Thông tin thí sinh:")
    print("Họ và tên:", thisinh[sbd][0])
    print("Điểm thi:", thisinh[sbd][1])
else:
    print("Không tìm thấy thí sinh. Nhập thông tin để bổ sung:")
    ten = input("Họ và tên: ")
    diem = float(input("Điểm thi: "))
    thisinh[sbd] = [ten, diem]
    print("Đã thêm thí sinh vào hệ thống.")