danh_sach_thi_sinh = {
    "01": {"Họ và tên": "Nguyễn Văn A", "Điểm thi": 8.5},
    "02": {"Họ và tên": "Trần Thị B", "Điểm thi": 7.0},
    "03": {"Họ và tên": "Lê Văn C", "Điểm thi": 9.0}
}
so_bao_danh = input("Nhập số báo danh: ")
if so_bao_danh in danh_sach_thi_sinh:
    print("Họ và tên: " + danh_sach_thi_sinh[so_bao_danh]['Họ và tên'])
    print("Điểm thi: " + str(danh_sach_thi_sinh[so_bao_danh]['Điểm thi']))
else:
    ho_ten = input("Nhập họ và tên thí sinh: ")
    diem_thi = float(input("Nhập điểm thi: "))
    danh_sach_thi_sinh[so_bao_danh] = {"Họ và tên": ho_ten, "Điểm thi": diem_thi}
    print("Đã thêm thí sinh mới vào danh sách.")