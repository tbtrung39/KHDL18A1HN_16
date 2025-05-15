def nhap_thong_tin():
    ho_ten = input("Nhập họ tên sinh viên: ")
    toan = float(input("Nhập điểm Toán: "))
    ly = float(input("Nhập điểm Lý: "))
    hoa = float(input("Nhập điểm Hóa: "))
    return ho_ten, toan, ly, hoa

def tinh_diem_trung_binh(toan, ly, hoa):
    return (toan + ly + hoa) / 3

def xuat_ket_qua(ho_ten, toan, ly, hoa, diem_tb):
    print("\n--- KẾT QUẢ ---")
    print(f"Họ tên: {ho_ten}")
    print(f"Điểm Toán: {toan}")
    print(f"Điểm Lý: {ly}")
    print(f"Điểm Hóa: {hoa}")
    print(f"Điểm trung bình: {diem_tb:.2f}")

ho_ten, toan, ly, hoa = nhap_thong_tin()
diem_tb = tinh_diem_trung_binh(toan, ly, hoa)
xuat_ket_qua(ho_ten, toan, ly, hoa, diem_tb)
