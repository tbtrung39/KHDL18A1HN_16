# Nhập thời gian sử dụng bóng đèn (giây)
time_in_seconds = float(input("Nhập thời gian sử dụng bóng đèn (giây): "))
V = 220  
I = 2.7  
price_per_kWh = 7000  
P = V * I  
E_wh = P * (time_in_seconds / 3600) 
cost = E_wh * price_per_kWh / 1000 
print(f"Tiền điện phải trả là: {cost:.2f} đồng")
