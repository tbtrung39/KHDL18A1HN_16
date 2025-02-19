# Nhập thông tin sinh viên
ma_so_sinh_vien = input("Nhập mã số sinh viên: ")
ho_ten = input("Nhập họ tên: ")
que_quan = input("Nhập quê quán: ")
nam_sinh = int(input("Nhập năm sinh: "))
diem_trung_binh = float(input("Nhập điểm trung bình các năm học: "))

# Xuất thông tin sinh viên
print("\nThông tin sinh viên:")
print(f"Mã số sinh viên: {ma_so_sinh_vien}")
print(f"Họ tên: {ho_ten}")
print(f"Quê quán: {que_quan}")
print(f"Năm sinh: {nam_sinh}")
print(f"Điểm trung bình các năm học: {diem_trung_binh:.2f}")
