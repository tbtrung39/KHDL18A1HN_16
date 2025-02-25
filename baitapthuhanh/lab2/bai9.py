electricity = float(input("Nhập số KW điện tiêu thụ: "))
if electricity <= 100:
    price = 2000
elif electricity <= 200:
    price = 2500
elif electricity <= 300:
    price = 3000
else:
    price = 5000
total_cost = electricity * price
print(f"Tiền điện phải trả: {total_cost} đồng")