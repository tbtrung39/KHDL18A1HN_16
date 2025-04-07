nhan_vien_dict = {}

n = int(input("Nhập số lượng nhân viên: "))

for _ in range(n):
    ma_nv = input("Nhập mã nhân viên (4 ký tự): ")
    ho_ten = input("Nhập họ tên nhân viên: ")
    nam_sinh = int(input("Nhập năm sinh của nhân viên: "))
    luong = int(input("Nhập lương của nhân viên: "))
    
    nhan_vien_dict[ma_nv] = {'HoTen': ho_ten, 'NamSinh': nam_sinh, 'Luong': luong}

ma_tim_kiem = input("Nhập mã nhân viên cần tìm: ")
if ma_tim_kiem in nhan_vien_dict:
    print(f"Thông tin nhân viên: {nhan_vien_dict[ma_tim_kiem]}")
else:
    print("Không tìm thấy nhân viên với mã này.")

ma_tang_luong = input("Nhập mã nhân viên để tăng lương: ")
if ma_tang_luong in nhan_vien_dict:
    nhan_vien_dict[ma_tang_luong]['Luong'] += 1000000
    print(f"Đã tăng lương cho nhân viên {ma_tang_luong}. Lương mới: {nhan_vien_dict[ma_tang_luong]['Luong']}")
else:
    print("Không tìm thấy nhân viên với mã này để tăng lương.")

ma_xoa = input("Nhập mã nhân viên cần xóa: ")
if ma_xoa in nhan_vien_dict:
    nhan_vien_dict.pop(ma_xoa)
    print(f"Nhân viên với mã {ma_xoa} đã bị xóa.")
else:
    print("Không tìm thấy nhân viên với mã này để xóa.")

sorted_nhan_vien = sorted(nhan_vien_dict.items(), key=lambda x: x[1]['NamSinh'], reverse=True)
print("Danh sách nhân viên sau khi sắp xếp theo năm sinh giảm dần:")
for ma_nv, thong_tin in sorted_nhan_vien:
    print(f"Mã: {ma_nv}, Họ tên: {thong_tin['HoTen']}, Năm sinh: {thong_tin['NamSinh']}, Lương: {thong_tin['Luong']}")