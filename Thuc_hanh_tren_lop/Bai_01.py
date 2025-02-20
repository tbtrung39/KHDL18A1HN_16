# Nhập thông tin sinh viên
ma_sinh_vien = input("Nhập mã số sinh viên: ")
ho_ten = input("Nhập họ tên sinh viên: ")
que_quan = input("Nhập quê quán sinh viên: ")
nam_sinh = int(input("Nhập năm sinh của sinh viên: "))
diem_tb = float(input("Nhập điểm trung bình các năm học: "))

# In kết quả
print("Thông tin sinh viên:")
print(f"Mã số sinh viên: {ma_sinh_vien}")
print(f"Họ tên: {ho_ten}")
print(f"Quê quán: {que_quan}")
print(f"Năm sinh: {nam_sinh}")
print(f"Điểm trung bình các năm học: {diem_tb}")