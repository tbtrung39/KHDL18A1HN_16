thu = int(input("Nhập thứ (1-7): "))

if not (1 <= thu <= 7):
    print("Thứ không hợp lệ.")
else:
    if thu == 1:
        ten_thu = "Chủ Nhật"
    elif thu == 2:
        ten_thu = "Thứ Hai"
    elif thu == 3:
        ten_thu = "Thứ Ba"
    elif thu == 4:
        ten_thu = "Thứ Tư"
    elif thu == 5:
        ten_thu = "Thứ Năm"
    elif thu == 6:
        ten_thu = "Thứ Sáu"
    else:
        ten_thu = "Thứ Bảy"

    print(f"Thứ {thu} là {ten_thu}.")