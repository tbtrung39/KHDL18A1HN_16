employees = {}

n = int(input("Nhập số lượng nhân viên: "))
for i in range(n):
    ma_nv = input("Nhập mã nhân viên (4 ký tự): ")
    ten = input("Nhập họ tên nhân viên (20 ký tự): ")
    nam_sinh = int(input("Nhập năm sinh của nhân viên: "))
    luong = float(input("Nhập lương của nhân viên: "))
    employees[ ma_nv] = {'Tên': ten, 'Năm sinh': nam_sinh, 'Lương': luong}

tim_ma_nv = input("Nhập mã nhân viên cần tìm: ")
if tim_ma_nv in employees:
    print(f"Thông tin nhân viên: {employees[tim_ma_nv]}")
else:
    print("Nhân viên không tồn tại.")

ma_nv_tang_luong = input("Nhập mã nhân viên cần tăng lương: ")
if ma_nv_tang_luong in employees:
    employees[ma_nv_tang_luong]['LươngLương'] += 1000000
    print(f"Lương của nhân viên {ma_nv_tang_luong} sau khi tăng: {employees[ma_nv_tang_luong]['Lương']}")
else:
    print("Nhân viên không tồn tại.")

xoa_ma_nv = input("Nhập mã nhân viên cần xóa: ")
if xoa_ma_nv in employees:
    del employees[xoa_ma_nv]
    print(f"Nhân viên với mã {xoa_ma_nv} đã bị xóa.")
else:
    print("Nhân viên không tồn tại.")

sorted_employees = dict(sorted(employees.items(), key=lambda x: x[1]['Năm sinh'], reverse=True))

print("\nDanh sách nhân viên sau khi sắp xếp giảm dần theo năm sinh:")
for ma_nv, details in sorted_employees.items():
    print(f"{ma_nv}: {details}")