start_hour = int(input("Nhập giờ bắt đầu (5-22): "))
end_hour = int(input("Nhập giờ kết thúc (5-22): "))
rental_rate = 100000
discount_rate = 0.75
peak_discount = 0.9
peak_start, peak_end = 11, 15
duration = end_hour - start_hour
if duration <= 3:
    total_cost = duration * rental_rate
else:
    total_cost = 3 * rental_rate + (duration - 3) * rental_rate * discount_rate
if peak_start <= start_hour < peak_end:
    total_cost *= peak_discount
print(f"Số tiền thuê sân phải trả: {total_cost} đồng")