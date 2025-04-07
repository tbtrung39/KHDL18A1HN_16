nhanvien = {}

n = int(input("Nhập số nhân viên: "))
for _ in range(n):
    ma = input("Mã NV (4 chữ số): ")
    hoten = input("Họ tên (20 ký tự): ")
    namsinh = int(input("Năm sinh: "))
    luong = int(input("Lương: "))
    nhanvien[ma] = [hoten, namsinh, luong]

x = input("Tìm kiếm mã nhân viên: ")
if x in nhanvien:
    print("Thông tin:", nhanvien[x])
else:
    print("Không tìm thấy.")

y = input("Nhập mã nhân viên cần tăng lương: ")
if y in nhanvien:
    nhanvien[y][2] += 1000000
    print("Đã tăng lương.")

z = input("Nhập mã nhân viên cần xóa: ")
if z in nhanvien:
    del nhanvien[z]
    print("Đã xóa.")

sapxep = sorted(nhanvien.items(), key=lambda x: x[1][1], reverse=True)
for nv in sapxep:
    print("Mã:", nv[0], "Tên:", nv[1][0], "Năm sinh:", nv[1][1], "Lương:", nv[1][2])
