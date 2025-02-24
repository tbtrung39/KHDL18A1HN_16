def ngay_tiep_theo(ngay, thang):
    so_ngay_trong_thang = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if ngay < so_ngay_trong_thang[thang]:
        ngay += 1
    else:
        ngay = 1
        thang += 1
        if thang > 12:
            thang = 1
    return ngay, thang
try:
    ngay = int(input("Nhap ngay: "))
    thang = int(input("Nhap thang: "))
    if 1 <= thang <= 12 and 1 <= ngay <= 31:
        ngay_moi, thang_moi = ngay_tiep_theo(ngay, thang)
        print(f"Ngay tiep theo la: {ngay_moi}/{thang_moi}")
    else:
        print("Ngay hoac thang khong hop le.")
except ValueError:
    print("Vui long nhap mot so nguyen hop le.")