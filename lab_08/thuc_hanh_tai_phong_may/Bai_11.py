def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    diem_toan = float(input("Nhập điểm Toán: "))
    diem_ly = float(input("Nhập điểm Lý: "))
    diem_hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, diem_toan, diem_ly, diem_hoa

def tinh_diem_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_ket_qua(ho_ten, dtb):
    print(f"Sinh viên: {ho_ten}")
    print(f"Điểm trung bình: {dtb:.2f}")

# Chương trình chính
ho_ten, toan, ly, hoa = nhap_thong_tin()
diem_tb = tinh_diem_trung_binh(toan, ly, hoa)
xuat_ket_qua(ho_ten, diem_tb)