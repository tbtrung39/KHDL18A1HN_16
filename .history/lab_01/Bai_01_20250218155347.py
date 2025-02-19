def nhap_thong_tin():
    hs = {}
    hs['Mã số sinh viên'] = input('Mã số sinh viên là: ')
    hs['Họ tên'] = input('Nhập họ tên: ')
    hs['Quê quán'] = input('Nhập quê quán: ')
    hs['Năm sinh'] = int(input('Nhập năm sinh: '))
    hs['Điểm trung bình'] = int(input('Nhập điểm trung bình: '))
    return hs
def xuat_thong_tin(hs):
    print("\nThông tin sinh viên:")
    print(f"Mã số sinh viên: {hs['Mã số sinh viên']}")
    print(f"Họ tên: {hs['Họ tên']}")
    print(f"Quê quán: {hs['Quê quán']}")
    print(f"Năm sinh: {hs['Năm sinh']}")
    print(f"Điểm trung bình: {hs['Điểm trung bình']}")
sinh_vien = nhap_thong_tin()
xuat_thong_tin(sinh_vien)
