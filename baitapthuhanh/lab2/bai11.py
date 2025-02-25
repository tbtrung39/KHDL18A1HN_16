day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if day < days_in_month[month - 1]:
    next_day = day + 1
    next_month = month
else:
    next_day = 1
    next_month = month + 1 if month < 12 else 1
print(f"Ngày tiếp theo là: {next_day}/{next_month}")
