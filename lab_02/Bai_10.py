start_hour = int(input("Nhập giờ bắt đầu (5-22): "))
end_hour = int(input("Nhập giờ kết thúc (5-22): "))

if start_hour < 5 or end_hour > 22 or start_hour >= end_hour:
    print("Giờ không hợp lệ!")
else:
    total_hours = end_hour - start_hour
    price_first_3 = 100000
    price_after_3 = price_first_3 * 0.75
    discount_time = (start_hour < 15 and end_hour > 11)

    if total_hours <= 3:
        total_price = total_hours * price_first_3
    else:
        total_price = 3 * price_first_3 + (total_hours - 3) * price_after_3

    if discount_time:
        total_price *= 0.9  # Giảm 10% nếu thuê trong khoảng 11-15 giờ

    print("Số tiền phải trả:", int(total_price), "đồng")
