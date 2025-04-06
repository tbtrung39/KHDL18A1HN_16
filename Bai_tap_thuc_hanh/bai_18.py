thi_sinh = {
    "001": {"ho_ten": "Nguyen Van A", "diem": 8},
    "002": {"ho_ten": "Tran Thi B", "diem": 9},
    "003": {"ho_ten": "Le Van C", "diem": 7}
}

so_bao_danh = input("Nhập số báo danh: ")

if so_bao_danh in thi_sinh:
    print("Họ và tên:", thi_sinh[so_bao_danh]["ho_ten"])
    print("Điểm thi:", thi_sinh[so_bao_danh]["diem"])
else:
    print("Không tìm thấy thí sinh.")
    ho_ten = input("Nhập họ và tên thí sinh: ")
    diem_thi = int(input("Nhập điểm thi: "))
    thi_sinh[so_bao_danh] = {"ho_ten": ho_ten, "diem": diem_thi}
    print("Đã thêm thông tin thí sinh.")