def ten_thang_trong_nam(thang):
    thang_trong_nam = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }
    return thang_trong_nam.get(thang, None)
while True:
    try:
        thang = int(input("Nhap thang (1-12): "))
        ten_thang = ten_thang_trong_nam(thang)
        if ten_thang:
            print(f"Thang {thang} la {ten_thang}.")
            break
        else:
            print("Thang khong hop le! Vui long nhap lai.")
    except ValueError:
        print("Vui long nhap mot so nguyen tu 1 den 12.")