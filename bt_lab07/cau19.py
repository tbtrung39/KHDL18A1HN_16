# a. Tạo mới từ điển
thong_tin_nhan_vien = {}
n_str = input("Nhập số lượng nhân viên n: ")
if n_str.isdigit():
    n = int(n_str)
    for _ in range(n):
        ma_nv = input("Nhập mã nhân viên (4 ký tự): ")
        ho_ten = input("Nhập họ tên nhân viên (20 ký tự): ")
        nam_sinh_str = input("Nhập năm sinh: ")
        luong_str = input("Nhập lương: ")
        if len(ma_nv) == 4 and ma_nv.isdigit():
            if len(ho_ten) <= 20:
                if nam_sinh_str.isdigit() and luong_str.isdigit():
                    thong_tin_nhan_vien[ma_nv] = {'ho_ten': ho_ten, 'nam_sinh': int(nam_sinh_str), 'luong': int(luong_str)}
                else:
                    print("Lỗi: Năm sinh và lương phải là số.")
            else:
                print("Lỗi: Họ tên không được quá 20 ký tự.")
        else:
            print("Lỗi: Mã nhân viên phải là 4 ký tự số.")
else:
    print("Lỗi: Số lượng nhân viên phải là số.")

# c. Tìm kiếm nhân viên với giá trị mã nhân viên là x
x = input("Nhập mã nhân viên cần tìm kiếm x: ")
if x in thong_tin_nhan_vien:
    print("Thông tin nhân viên có mã", x + ":")
    print("Họ tên:", thong_tin_nhan_vien[x]['ho_ten'])
    print("Năm sinh:", thong_tin_nhan_vien[x]['nam_sinh'])
    print("Lương:", thong_tin_nhan_vien[x]['luong'])
else:
    print("Không tìm thấy nhân viên có mã", x)

# b. Thêm nhân viên với các thông tin được nhập từ bàn phím
them_tiep = input("Bạn có muốn thêm nhân viên (y/n)? ")
if them_tiep.lower() == 'y':
    ma_nv_moi = input("Nhập mã nhân viên mới (4 ký tự): ")
    if ma_nv_moi not in thong_tin_nhan_vien:
        ho_ten_moi = input("Nhập họ tên nhân viên mới (20 ký tự): ")
        nam_sinh_moi_str = input("Nhập năm sinh mới: ")
        luong_moi_str = input("Nhập lương mới: ")
        if len(ma_nv_moi) == 4 and ma_nv_moi.isdigit():
            if len(ho_ten_moi) <= 20:
                if nam_sinh_moi_str.isdigit() and luong_moi_str.isdigit():
                    thong_tin_nhan_vien[ma_nv_moi] = {'ho_ten': ho_ten_moi, 'nam_sinh': int(nam_sinh_moi_str), 'luong': int(luong_moi_str)}
                    print("Đã thêm nhân viên mới.")
                else:
                    print("Lỗi: Năm sinh và lương phải là số.")
            else:
                print("Lỗi: Họ tên không được quá 20 ký tự.")
        else:
            print("Lỗi: Mã nhân viên phải là 4 ký tự số.")
    else:
        print("Lỗi: Mã nhân viên đã tồn tại.")

# d. Tăng lương 1000000 cho nhân viên có mã là y
y = input("Nhập mã nhân viên cần tăng lương y: ")
if y in thong_tin_nhan_vien:
    thong_tin_nhan_vien[y]['luong'] += 1000000
    print("Đã tăng lương cho nhân viên có mã", y)
else:
    print("Không tìm thấy nhân viên có mã", y)

# e. Xóa nhân viên có mã là z
z = input("Nhập mã nhân viên cần xóa z: ")
if z in thong_tin_nhan_vien:
    del thong_tin_nhan_vien[z]
    print("Đã xóa nhân viên có mã", z)
else:
    print("Không tìm thấy nhân viên có mã", z)