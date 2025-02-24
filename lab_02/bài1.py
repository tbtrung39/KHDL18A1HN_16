def so_ngay_trong_thang(thang):
    so_ngay = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if thang in so_ngay:
        return so_ngay[thang]
    else:
        return None
try:
    thang = int(input("Nhap thang (1-12): "))
    ngay = so_ngay_trong_thang(thang)
    if ngay:
        print(f"Thang {thang} co {ngay} ngay.")
    else:
        print("Thang khang hop le! Vui long nhap tu 1 đen 12.")
except ValueError:
    print("Vui long nhap mot so nguyen tu 1 den 12.")