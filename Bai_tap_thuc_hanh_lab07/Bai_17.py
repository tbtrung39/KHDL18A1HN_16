n = int(input("Nhập số lượng sinh viên: "))
sinh_vien = {}

for _ in range(n):
    ma = input("Nhập mã sinh viên (6 chữ số): ")
    ten = input("Nhập tên sinh viên: ")
    diem = float(input("Nhập điểm: "))
    diem = round(diem)
    sinh_vien[ma] = (ten, diem)

ds = list(sinh_vien.items())
ds.sort(key=lambda x: x[1][1], reverse=True)

for sv in ds:
    print("Mã:", sv[0], "Tên:", sv[1][0], "Điểm:", sv[1][1])
