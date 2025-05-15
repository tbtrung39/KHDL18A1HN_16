def tinh_tb(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_thong_tin(ho_ten, toan, ly, hoa):
    dtb = tinh_tb(toan, ly, hoa)
    print(f"Họ tên: {ho_ten}")
    print(f"Toán: {toan}, Lý: {ly}, Hóa: {hoa}")
    print(f"Điểm trung bình: {dtb:.2f}")

ho_ten = input("Nhập họ tên sinh viên: ")
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))

xuat_thong_tin(ho_ten, toan, ly, hoa)