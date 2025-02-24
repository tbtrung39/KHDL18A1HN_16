def ten_thu_trong_tuan(thu):
    thu_trong_tuan = {
        1: "Sunday",
        2: "Monday",
        3: "Tuesday",
        4: "Wednesday",
        5: "Thursday",
        6: "Friday",
        7: "Saturday"
    }
    return thu_trong_tuan.get(thu, None)
while True:
    try:
        thu = int(input("Nhap thu (1-7): "))
        ten_thu = ten_thu_trong_tuan(thu)
        if ten_thu:
            print(f"Thu {thu} la {ten_thu}.")
            break
        else:
            print("Thu khong hop le! Vui long nhap lai.")
    except ValueError:
        print("Vui long nhap mot so nguyen tu 1 den 7.")