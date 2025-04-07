# Tạo từ điển dữ liệu sinh viên
sinh_vien = {
    '001001': {'ho_ten': 'Nguyen Van A', 'diem': 9},
    '001002': {'ho_ten': 'Le Thi B', 'diem': 7},
    '001003': {'ho_ten': 'Tran Van C', 'diem': 8}
}

# Nhập mã số cần tra
ma_tra = input("Nhập mã số sinh viên cần tra: ")

# Tra cứu bằng vòng lặp (không dùng in, get,...)
tim_thay = False
for ma in sinh_vien:
    if ma == ma_tra:
        print("Tìm thấy sinh viên:")
        print("Họ tên:", sinh_vien[ma]['ho_ten'])
        print("Điểm thi:", sinh_vien[ma]['diem'])
        tim_thay = True
        break

if tim_thay == False:
    print("Không tìm thấy sinh viên.")