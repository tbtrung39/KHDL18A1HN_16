def xep_loai_hoc_luc(diem):
    if 0.0 <= diem <= 3.0:
        return "Loai Kem"
    elif diem == 4.0:
        return "Loai Yeu"
    elif 5.0 <= diem <= 6.0:
        return "Loai Trung binh"
    elif 7.0 <= diem <= 8.0:
        return "Loai Kha"
    elif 9.0 <= diem <= 10.0:
        return "Loai Gioi"
    else:
        return "Diem khong hop le"
try:
    diem = float(input("Nhap diem tong ket: "))
    print(f"Hoc luc cua hoc sinh la: {xep_loai_hoc_luc(diem)}")
except ValueError:
    print("Vui long nhap mot diem hop le.")