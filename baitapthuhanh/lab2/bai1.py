month = int(input("Nhập tháng (1-12): "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if 1 <= month <= 12:
    print(f"Tháng {month} có {days_in_month[month - 1]} ngày.")
else:
    print("Tháng không hợp lệ.")