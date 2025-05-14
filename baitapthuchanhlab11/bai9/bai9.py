def quan_ly_checkin(tep_passengers, tep_weight_out, tep_canceled_out):
    with open(tep_passengers, 'r') as f_passengers:
        num_khach = int(f_passengers.readline())
        thong_tin_khach = [line.strip() for line in f_passengers]

    with open(tep_weight_out, 'w') as f_weight:
        pass

    with open(tep_canceled_out, 'w') as f_canceled:
        pass

    print("Thông tin hành khách và kết quả kiểm tra:")
    khach_huy_chuyen = []

    with open(tep_weight_out, 'w') as f_weight, open(tep_canceled_out, 'w') as f_canceled:
        for i in range(num_khach):
            info = thong_tin_khach[i].split()
            so_luong_tay = len(info)
            tong_trong_luong = sum(float(w) for w in info)

            f_weight.write(f"{tong_trong_luong:.2f}\n")
            print(f"Khách {i+1}: Số lượng tay = {so_luong_tay}, Tổng trọng lượng = {tong_trong_luong:.2f} kg")

            if tong_trong_luong > 23 or so_luong_tay > 5:
                khach_huy_chuyen.append(i + 1)
                f_canceled.write(str(i + 1) + '\n')

    if khach_huy_chuyen:
        print("\nCác hành khách bị hủy chuyến:")
        for stt in khach_huy_chuyen:
            print(f"- Khách {stt}")
    else:
        print("\nKhông có hành khách nào bị hủy chuyến.")
ten_tep_passenger = 'KHDL18A1HN_16/baitapthuchanhlab11/bai9/PASSENGER.IN'
ten_tep_weight_out = 'KHDL18A1HN_16/baitapthuchanhlab11/bai9/WEIGHT.OUT'
ten_tep_canceled_out = 'KHDL18A1HN_16/baitapthuchanhlab11/bai9/CANCELED.OUT'
quan_ly_checkin(ten_tep_passenger, ten_tep_weight_out, ten_tep_canceled_out)